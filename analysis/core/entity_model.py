def build_entity_model(
    dependency_graph,
    associations,
    method_graph
):

    entities = {}

    # =========================
    # IMPORTS
    # =========================
    from analysis.core.entity_normalizer import normalize_entity
    from analysis.core.entity_filter import (
        is_valid_domain_entity,
        is_framework
    )

    # =========================
    # SAFE GET
    # =========================
    def safe_get(graph, key):
        return graph.get(key, {}) if isinstance(graph, dict) else {}

    # =========================
    # METHODS RESOLVER
    # =========================
    def get_methods(model):

        if not isinstance(method_graph, dict):
            return []

        if model in method_graph and isinstance(method_graph[model], list):
            return method_graph[model] or []

        for section in ("domain", "framework"):
            section_data = method_graph.get(section, {})
            if isinstance(section_data, dict):
                methods = section_data.get(model, [])
                if isinstance(methods, list):
                    return methods

        return []

    # =========================
    # COLLECT MODELS (DETERMINISTIC)
    # =========================
    all_models = set()

    if isinstance(dependency_graph, dict):
        all_models.update(dependency_graph.keys())

    if isinstance(method_graph, dict):
        for v in method_graph.values():
            if isinstance(v, dict):
                all_models.update(v.keys())

    if isinstance(associations, dict):
        all_models.update(associations.keys())

    # deterministic ordering
    all_models = sorted(all_models)

    # =========================
    # BUILD ENTITIES
    # =========================
    for raw_model in all_models:

        model = normalize_entity(raw_model)
        if not model:
            continue

        # framework filter
        if is_framework(model):
            continue

        if not is_valid_domain_entity(model):
            continue

        entities[model] = {
            "methods": [],
            "dependencies": [],
            "associations": {}
        }

        # =========================
        # METHODS
        # =========================
        raw_methods = get_methods(model)

        if isinstance(raw_methods, list):
            entities[model]["methods"] = sorted(
                [m for m in raw_methods if isinstance(m, str) and m.strip()]
            )

        # =========================
        # DEPENDENCIES
        # =========================
        deps = safe_get(dependency_graph, model)

        if isinstance(deps, list):

            clean = []
            seen = set()

            for d in deps:

                name = d.get("name") if isinstance(d, dict) else d
                name = normalize_entity(name)

                if not name or name in seen:
                    continue

                clean.append(name)
                seen.add(name)

            entities[model]["dependencies"] = sorted(clean)

        # =========================
        # ASSOCIATIONS
        # =========================
        assoc_data = safe_get(associations, model)

        if isinstance(assoc_data, dict):

            normalized = {}

            for assoc_type, targets in assoc_data.items():

                if not isinstance(targets, list):
                    continue

                clean = []
                seen = set()

                for t in targets:

                    t = normalize_entity(t)

                    if not t or t in seen:
                        continue

                    clean.append(t)
                    seen.add(t)

                normalized[assoc_type] = sorted(clean)

            entities[model]["associations"] = normalized

    return entities