from analysis.graph_builder import build_graph
from analysis.association_parser import (
    parse_associations
)


def merge_graphs(
    controller_file,
    model_files
):

    merged = {
        "controller": controller_file,
        "models": {}
    }

    # dependency graph
    graph = build_graph(controller_file)

    for model, methods in graph.items():

        merged["models"][model] = {
            "methods": methods,
            "associations": {}
        }

    # associations
    for model_file in model_files:

        assoc_data = parse_associations(
            model_file
        )

        source_model = assoc_data["model"]

        if source_model not in merged["models"]:
            continue

        merged["models"][source_model][
            "associations"
        ] = assoc_data["associations"]

    return merged