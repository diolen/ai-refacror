def build_dependency_index(entity_model):
    """
    Creates adjacency list:
    entity -> direct dependencies
    """

    index = {}

    if not isinstance(entity_model, dict):
        return index

    for entity, data in entity_model.items():

        deps = data.get("dependencies", [])

        if not isinstance(deps, list):
            continue

        clean = []

        for d in deps:
            if isinstance(d, dict):
                name = d.get("name")
            else:
                name = d

            if isinstance(name, str) and name.strip():
                clean.append(name.strip())

        index[entity] = clean

    return index


def propagate_dependencies(entity_model, max_depth=5):
    """
    Expands dependencies transitively:
    A -> B -> C becomes A -> [B, C]
    """

    if not isinstance(entity_model, dict):
        return entity_model

    index = build_dependency_index(entity_model)

    def dfs(node, visited, depth):
        if depth > max_depth:
            return set()

        if node not in index:
            return set()

        result = set()

        for dep in index.get(node, []):
            if dep in visited:
                continue

            result.add(dep)
            visited.add(dep)

            result.update(dfs(dep, visited, depth + 1))

        return result

    new_model = {}

    for entity, data in entity_model.items():

        if not isinstance(data, dict):
            continue

        base_deps = data.get("dependencies", [])
        clean_base = []

        for d in base_deps:
            if isinstance(d, dict):
                name = d.get("name")
            else:
                name = d

            if isinstance(name, str):
                clean_base.append(name)

        propagated = set(clean_base)

        for dep in clean_base:
            propagated.update(dfs(dep, set([entity]), 1))

        new_model[entity] = {
            **data,
            "dependencies": sorted(propagated)
        }

    return new_model