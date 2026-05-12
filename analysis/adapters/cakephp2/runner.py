import json

from analysis.adapters.cakephp2.dependency_scan import scan_dependencies
from analysis.adapters.cakephp2.association_parser import parse_associations
from analysis.adapters.cakephp2.graph_builder import build_graph

from analysis.core.entity_model import build_entity_model
from analysis.core.entity_enricher import enrich_entity_model
from analysis.core.impact_engine import (
    compute_entity_impact,
    print_impact,
    print_entity_model
)
from analysis.core.entity_normalizer import normalize_entity_model

from analysis.core.prompt_builder.entity_prompt import EntityPrompt
from analysis.core.prompt_builder.impact_prompt import ImpactPrompt
from analysis.core.prompt_builder.refactor_prompt import RefactorPrompt
from analysis.core.prompt_builder.prompt_renderer import render_prompt
from analysis.core.prompt_builder.prompt_context import PromptContext


# =========================
# SCAN
# =========================
def run_scan(args):

    controller_file = args.file

    result = scan_dependencies(controller_file)

    print(json.dumps(result, indent=2, ensure_ascii=False))

    return 0


# =========================
# SHARED PIPELINE (FIX)
# =========================
def _build_analysis(controller_file, model_file):

    scan_result = scan_dependencies(controller_file)
    deps_raw = scan_result.get("dependencies", [])

    dependency_graph = {}

    for d in deps_raw:
        name = d.get("name")
        if isinstance(name, str):
            dependency_graph.setdefault(name, []).append(name)

    assoc_result = parse_associations(model_file)

    associations = {
        assoc_result["model"]: assoc_result["associations"]
    }

    method_graph = build_graph(controller_file).get("domain", {})

    entity_model = build_entity_model(
        dependency_graph=dependency_graph,
        associations=associations,
        method_graph=method_graph,
    )

    entity_model = normalize_entity_model(entity_model)

    entity_model = enrich_entity_model(
        entity_model=entity_model,
        scan_result=scan_result,
        method_graph=method_graph
    )

    return entity_model, scan_result, method_graph


# =========================
# IMPACT
# =========================
def run_impact(args):

    entity_name = args.entity

    entity_model, scan_result, method_graph = _build_analysis(
        args.controller,
        args.model
    )

    print_entity_model(entity_model)

    result = compute_entity_impact(entity_name, entity_model)

    if result is None:
        print(json.dumps({
            "error": f"Entity '{entity_name}' not found",
            "available": sorted(entity_model.keys())
        }, indent=2, ensure_ascii=False))
        return 1

    print_impact(result)

    context = PromptContext()

    context.update(
        impact_score=result.get("score"),
        connectivity=result.get("connectivity"),
        connectivity_breakdown=result.get("connectivity_breakdown", {}),
        insights=result.get("insights", []),
        risk_score=result.get("score")
    )

    prompt = ImpactPrompt(
        entity_model=entity_model,
        context=context.get()
    ).build(entity_name)

    print("\n" + "=" * 60)
    print("LLM PROMPT (IMPACT)")
    print("=" * 60)
    print(render_prompt(prompt))
    print("=" * 60 + "\n")

    return 0


# =========================
# MERGE
# =========================
def run_merge(args):

    entity_model, _, _ = _build_analysis(
        args.controller,
        args.model
    )

    print_entity_model(entity_model)

    prompt = EntityPrompt(entity_model).build()

    print("\n" + "=" * 60)
    print("LLM PROMPT (ENTITY MODEL)")
    print("=" * 60)
    print(render_prompt(prompt))
    print("=" * 60 + "\n")

    return 0


# =========================
# PROMPT MODE (FIXED + CLEAN)
# =========================
def run_prompt(args):

    entity_name = args.entity

    entity_model, scan_result, method_graph = _build_analysis(
        args.controller,
        args.model
    )

    impact_result = compute_entity_impact(entity_name, entity_model)

    if impact_result is None:
        print(json.dumps({
            "error": f"Entity '{entity_name}' not found",
            "available": sorted(entity_model.keys())
        }, indent=2, ensure_ascii=False))
        return 1

    context = PromptContext()

    context.update(
        impact_score=impact_result.get("score"),
        connectivity=impact_result.get("connectivity"),
        connectivity_breakdown=impact_result.get("connectivity_breakdown", {}),
        insights=impact_result.get("insights", []),
        risk_score=impact_result.get("score")
    )

    if args.mode == "impact":

        builder = ImpactPrompt(
            entity_model=entity_model,
            context=context.get()
        )

    else:

        builder = RefactorPrompt(
            entity_model=entity_model,
            context=context.get()
        )

    prompt = builder.build(entity_name)

    print("\n" + "=" * 60)
    print(f"LLM PROMPT ({args.mode.upper()})")
    print("=" * 60)

    print(render_prompt(prompt))

    print("=" * 60 + "\n")

    return 0


# =========================
# RUNTIME ENTITY MODEL
# =========================
def build_runtime_entity_model(controller_file, model_file):

    scan_result = scan_dependencies(controller_file)

    deps_raw = scan_result.get("dependencies", [])

    dependency_graph = {}

    for d in deps_raw:

        name = d.get("name")

        if isinstance(name, str):
            dependency_graph.setdefault(name, []).append(name)

    assoc_result = parse_associations(model_file)

    associations = {
        assoc_result["model"]: assoc_result["associations"]
    }

    method_graph = build_graph(controller_file).get("domain", {})

    entity_model = build_entity_model(
        dependency_graph=dependency_graph,
        associations=associations,
        method_graph=method_graph,
    )

    entity_model = normalize_entity_model(entity_model)

    entity_model = enrich_entity_model(
        entity_model=entity_model,
        scan_result=scan_result,
        method_graph=method_graph
    )

    return entity_model