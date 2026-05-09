from collections import defaultdict


def build_propagation_graph(entity_model):
    """
    Builds transitive dependency graph:
    A -> B -> C propagation tracking
    """

    if not isinstance(entity_model, dict):
        return {}

    graph = defaultdict(set)

    # =========================
    # STEP 1: direct dependencies
    # =========================
    for entity, data in entity_model.items():

        if not isinstance(data, dict):
            continue

        deps = data.get("dependencies", [])
        if not isinstance(deps, list):
            continue

        for dep in deps:
            if isinstance(dep, str):
                graph[entity].add(dep)

    return dict(graph)


def propagate_dependencies(graph, max_depth=3):
    """
    Expands dependency graph transitively.

    Example:
    A -> B
    B -> C
    Result:
    A -> B, C
    """

    if not isinstance(graph, dict):
        return {}

    expanded = {}

    def dfs(node, visited, depth):
        if depth > max_depth:
            return set()

        result = set()

        for neighbor in graph.get(node, []):
            if neighbor in visited:
                continue

            result.add(neighbor)
            visited.add(neighbor)

            result |= dfs(neighbor, visited, depth + 1)

        return result

    for node in graph:
        expanded[node] = list(dfs(node, set([node]), 0))

    return expanded


def merge_propagation_into_entity_model(entity_model, propagated_graph):
    """
    Adds propagated dependencies without breaking existing structure
    """

    if not isinstance(entity_model, dict):
        return entity_model

    for entity, data in entity_model.items():

        if not isinstance(data, dict):
            continue

        direct = set(data.get("dependencies", []))
        propagated = set(propagated_graph.get(entity, []))

        data["propagated_dependencies"] = sorted(list(propagated - direct))

        # optional signal for impact engine later
        data["total_dependency_span"] = len(direct | propagated)

    return entity_model