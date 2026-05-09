from analysis.adapters.cakephp2.dependency_scan import (
    scan_dependencies
)

from analysis.adapters.cakephp2.graph_builder import (
    build_graph
)

from analysis.adapters.cakephp2.association_parser import (
    parse_associations
)

from analysis.core.entity_model import (
    build_entity_model
)

from analysis.core.entity_normalizer import (
    normalize_entity_model
)

from analysis.core.entity_enricher import enrich_entity_model

from analysis.core.dependency_propagation_engine import (
    propagate_dependencies
)


def analyze_file(controller_file, model_file):

    dependency_graph = scan_dependencies(
        controller_file
    )

    method_graph = build_graph(
        controller_file
    )

    assoc_data = parse_associations(
        model_file
    )

    associations = {
        assoc_data["model"]:
        assoc_data["associations"]
    }

    entity_model = build_entity_model(
        {d["name"]: [d] for d in dependency_graph["dependencies"]},
        associations,
        method_graph
    )

    entity_model = normalize_entity_model(entity_model)

    entity_model = enrich_entity_model(
        entity_model=entity_model,
        scan_result=dependency_graph,
        method_graph=method_graph
    )

    # =========================
    # DEPENDENCY PROPAGATION LAYER (NEW)
    # =========================
    entity_model = propagate_dependencies(entity_model)

    return entity_model