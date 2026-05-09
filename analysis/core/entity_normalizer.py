def normalize_entity(value):
    if value is None:
        return ""

    if not isinstance(value, str):
        value = str(value)

    token = value.strip()
    if not token:
        return ""

    # Drop common PHP wrappers to keep stable entity keys.
    token = token.lstrip("$")
    token = token.split("->")[-1]
    token = token.split("::")[-1]
    token = token.split("\\")[-1]

    if token.endswith(".php"):
        token = token[:-4]

    return token.strip()


def normalize_entity_model(raw_entity_model):

    if not isinstance(raw_entity_model, dict):
        return {}

    normalized = {}

    for name, data in raw_entity_model.items():

        name = normalize_entity(name)
        if not name:
            continue

        if not isinstance(data, dict):
            continue

        # =========================
        # METHODS (ONLY CLEAN PASS)
        # =========================
        raw_methods = data.get("methods", [])

        methods = []
        seen_methods = set()

        for m in raw_methods:
            m = normalize_entity(m)

            if not m:
                continue

            # dedup
            if m in seen_methods:
                continue

            seen_methods.add(m)
            methods.append(m)

        # =========================
        # DEPENDENCIES
        # =========================
        raw_deps = data.get("dependencies", [])

        deps = []
        seen_deps = set()

        for d in raw_deps:

            d = normalize_entity(d)

            if not d:
                continue

            if d == name:
                continue

            if d in seen_deps:
                continue

            seen_deps.add(d)
            deps.append(d)

        # =========================
        # ASSOCIATIONS (SAFE COPY)
        # =========================
        raw_assoc = data.get("associations", {})

        associations = {}

        if isinstance(raw_assoc, dict):

            for assoc_type, targets in raw_assoc.items():

                if not isinstance(targets, list):
                    continue

                clean_targets = []
                seen_targets = set()

                for t in targets:

                    t = normalize_entity(t)

                    if not t:
                        continue

                    if t in seen_targets:
                        continue

                    seen_targets.add(t)
                    clean_targets.append(t)

                associations[assoc_type] = clean_targets

        # =========================
        # FINAL ENTITY
        # =========================
        normalized[name] = {
            "methods": methods,
            "dependencies": deps,
            "associations": associations
        }

    return normalized