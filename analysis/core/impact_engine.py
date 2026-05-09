def compute_entity_impact(entity_name, entity_model):

    if entity_name not in entity_model:
        return None

    entity = entity_model[entity_name]

    methods = entity.get("methods", [])
    dependencies = entity.get("dependencies", [])
    associations = entity.get("associations", {})

    # =========================
    # WEIGHTS
    # =========================
    WEIGHTS = {
        "method": 1.2,
        "dependency": 2.0,
        "hasMany": 3.0,
        "belongsTo": 2.0,
        "hasOne": 1.5,
        "hasAndBelongsToMany": 4.0
    }

    # =========================
    # CLEAN DEPENDENCIES
    # =========================
    clean_dependencies = []

    for d in dependencies:
        if isinstance(d, dict):
            name = d.get("name")
        else:
            name = d

        if isinstance(name, str):
            clean_dependencies.append(name)

    # =========================
    # BASE SCORE
    # =========================
    score = 0.0

    score += len(methods) * WEIGHTS["method"]
    score += len(clean_dependencies) * WEIGHTS["dependency"]

    score += len(associations.get("hasMany", [])) * WEIGHTS["hasMany"]
    score += len(associations.get("belongsTo", [])) * WEIGHTS["belongsTo"]
    score += len(associations.get("hasOne", [])) * WEIGHTS["hasOne"]
    score += len(associations.get("hasAndBelongsToMany", [])) * WEIGHTS["hasAndBelongsToMany"]

    # =========================
    # CONNECTIVITY
    # =========================
    connected_nodes = set(clean_dependencies)

    for targets in associations.values():
        if isinstance(targets, list):
            for t in targets:
                if isinstance(t, str):
                    connected_nodes.add(t)

    connectivity = len(connected_nodes)

    # =========================
    # NONLINEAR BOOST
    # =========================
    score += (len(methods) * 0.4) * (1 + min(connectivity, 10) * 0.1)

    # =========================
    # BUSINESS METHODS
    # =========================
    business_methods = [
        m for m in methods
        if isinstance(m, str)
        and not m.lower().startswith(("get", "set", "is", "find", "read"))
    ]

    score += min(len(business_methods), 10) * 0.8

    # =========================
    # INSIGHTS
    # =========================
    insights = []

    if connectivity >= 5:
        insights.append(f"{entity_name} is highly connected domain node")

    if len(clean_dependencies) >= 3:
        insights.append(f"{entity_name} has high external coupling")

    if len(associations.get("hasMany", [])) >= 2:
        insights.append(f"{entity_name} is aggregation root candidate")

    if len(business_methods) >= 5:
        insights.append(f"{entity_name} contains rich domain logic")

    if score >= 18:
        insights.append(f"{entity_name} is CRITICAL refactor risk")

    elif score >= 10:
        insights.append(f"{entity_name} is MEDIUM complexity entity")

    return {
        "model": entity_name,
        "score": round(score, 2),
        "methods": methods,
        "dependencies": clean_dependencies,
        "associations": associations,
        "insights": insights,
        "connectivity": connectivity
    }


# =========================
# HUMAN READABLE OUTPUT
# =========================
def print_impact(result):

    if not result:
        print("No data found")
        return

    print("\n" + "=" * 60)
    print(f"IMPACT ANALYSIS: {result['model']}")
    print("=" * 60)

    print(f"\nScore: {result['score']}")
    print(f"Connectivity: {result.get('connectivity', 0)}")

    print("\nMethods:")
    if result["methods"]:
        for m in result["methods"]:
            print(f"  - {m}")
    else:
        print("  (none)")

    print("\nDependencies:")
    if result["dependencies"]:
        for d in result["dependencies"]:
            print(f"  - {d}")
    else:
        print("  (none)")

    print("\nAssociations:")

    assoc = result.get("associations", {})

    for key in ["hasMany", "belongsTo", "hasOne", "hasAndBelongsToMany"]:
        print(f"  {key}:")

        values = assoc.get(key, [])
        if values:
            for v in values:
                print(f"    - {v}")
        else:
            print("    (none)")

    print("\nInsights:")
    if result["insights"]:
        for i in result["insights"]:
            print(f"  • {i}")
    else:
        print("  (none)")

    print("\n" + "=" * 60 + "\n")

def print_entity_model(entity_model):

    if not entity_model:
        print("No entities found")
        return

    print("\n" + "=" * 60)
    print("ENTITY MODEL")
    print("=" * 60)

    for entity_name, data in entity_model.items():

        print(f"\nEntity: {entity_name}")

        # =========================
        # METHODS
        # =========================
        print("\n  Methods:")

        methods = data.get("methods", [])

        if methods:
            for m in methods:
                print(f"    - {m}")
        else:
            print("    (none)")

        # =========================
        # DEPENDENCIES
        # =========================
        print("\n  Dependencies:")

        deps = data.get("dependencies", [])

        if deps:
            for d in deps:
                print(f"    - {d}")
        else:
            print("    (none)")

        # =========================
        # ASSOCIATIONS
        # =========================
        print("\n  Associations:")

        assoc = data.get("associations", {})

        for assoc_type in [
            "hasMany",
            "belongsTo",
            "hasOne",
            "hasAndBelongsToMany"
        ]:

            print(f"\n    {assoc_type}:")

            values = assoc.get(assoc_type, [])

            if values:
                for v in values:
                    print(f"      - {v}")
            else:
                print("      (none)")

        print("\n" + "-" * 60)