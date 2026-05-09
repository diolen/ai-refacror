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


# =========================
# PROMPT BUILDER (NEW)
# =========================
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
# IMPACT
# =========================
def run_impact(args):

    entity_name = args.entity
    controller_file = args.controller
    model_file = args.model

    scan_result = scan_dependencies(controller_file)
    deps_raw = scan_result.get("dependencies", [])

    dependency_graph = {}
    for d in deps_raw:
        name = d.get("name")
        if isinstance(name, str):
            dependency_graph.setdefault(name, []).append(name)

    assoc_result = parse_associations(model_file)
    associations = assoc_result.get("associations", {})

    method_graph = build_graph(controller_file).get("domain", {})

    # =========================
    # BUILD ENTITY MODEL
    # =========================
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

    print_entity_model(entity_model)

    # =========================
    # IMPACT CALCULATION
    # =========================
    result = compute_entity_impact(entity_name, entity_model)

    if result is None:
        print(json.dumps({
            "error": f"Entity '{entity_name}' not found",
            "available": sorted(entity_model.keys())
        }, indent=2, ensure_ascii=False))
        return 1

    print_impact(result)

    # =========================
    # PROMPT BUILDER INTEGRATION (NEW)
    # =========================
    context = PromptContext()

    context.update(
        impact_score=result.get("score"),
        connectivity=result.get("connectivity"),
        insights=result.get("insights", [])
    )

    impact_prompt = ImpactPrompt(
        entity_model=entity_model,
        context=context.get()
    )

    prompt = impact_prompt.build(entity_name)

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

    controller_file = args.controller
    model_file = args.model

    scan_result = scan_dependencies(controller_file)
    dependencies = scan_result.get("dependencies", [])

    assoc_result = parse_associations(model_file)

    associations = {
        assoc_result["model"]: assoc_result["associations"]
    }

    raw_graph = build_graph(controller_file)
    method_graph = raw_graph.get("domain", {})

    entity_model = build_entity_model(
        dependency_graph={
            d["name"]: [d]
            for d in dependencies
            if isinstance(d, dict) and "name" in d
        },
        associations=associations,
        method_graph=method_graph
    )

    entity_model = normalize_entity_model(entity_model)
    entity_model = enrich_entity_model(
        entity_model=entity_model,
        scan_result=scan_result,
        method_graph=raw_graph
    )

    print_entity_model(entity_model)

    # =========================
    # PROMPT BUILDER (MERGE MODE)
    # =========================
    context = PromptContext()

    entity_prompt = EntityPrompt(entity_model)
    prompt = entity_prompt.build()

    print("\n" + "=" * 60)
    print("LLM PROMPT (ENTITY MODEL)")
    print("=" * 60)
    print(render_prompt(prompt))
    print("=" * 60 + "\n")

    return 0