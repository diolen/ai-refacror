def compute_entity_impact(entity_name, entity_model):

    if not isinstance(entity_model, dict):
        return None

    if entity_name not in entity_model:
        return None

    entity = entity_model.get(entity_name, {})

    methods = entity.get("methods", []) or []
    dependencies = entity.get("dependencies", []) or []
    associations = entity.get("associations", {}) or {}

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

        if isinstance(name, str) and name.strip():
            clean_dependencies.append(name)

    # =========================
    # BASE SCORE
    # =========================
    score = 0.0

    score += len(methods) * WEIGHTS["method"]
    score += len(clean_dependencies) * WEIGHTS["dependency"]

    score += len(associations.get("hasMany", []) or []) * WEIGHTS["hasMany"]
    score += len(associations.get("belongsTo", []) or []) * WEIGHTS["belongsTo"]
    score += len(associations.get("hasOne", []) or []) * WEIGHTS["hasOne"]
    score += len(associations.get("hasAndBelongsToMany", []) or []) * WEIGHTS["hasAndBelongsToMany"]

    # =========================
    # CONNECTIVITY MODEL
    # =========================
    dependency_connectivity = len(clean_dependencies)

    association_connectivity = (
        len(associations.get("hasMany", []) or []) * WEIGHTS["hasMany"] +
        len(associations.get("belongsTo", []) or []) * WEIGHTS["belongsTo"] +
        len(associations.get("hasOne", []) or []) * WEIGHTS["hasOne"] +
        len(associations.get("hasAndBelongsToMany", []) or []) * WEIGHTS["hasAndBelongsToMany"]
    )

    behavioral_connectivity = len(methods)

    connectivity = (
        dependency_connectivity +
        association_connectivity +
        behavioral_connectivity
    )

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
        and m.strip()
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

    if len(associations.get("hasMany", []) or []) >= 2:
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
        "connectivity": round(connectivity, 2),
        "connectivity_breakdown": {
            "dependency": dependency_connectivity,
            "association": association_connectivity,
            "behavioral": behavioral_connectivity
        }
    }


# =========================
# OUTPUT LAYER
# =========================

def print_impact(result):

    if not result:
        print("No data found")
        return

    print("\n" + "=" * 60)
    print(f"IMPACT ANALYSIS: {result.get('model')}")
    print("=" * 60)

    print(f"\nScore: {result.get('score', 0)}")
    print(f"Connectivity: {result.get('connectivity', 0)}")

    print("\nMethods:")
    for m in result.get("methods", []):
        print(f"  - {m}")

    print("\nDependencies:")
    for d in result.get("dependencies", []):
        print(f"  - {d}")

    print("\nAssociations:")
    assoc = result.get("associations", {}) or {}

    for key in ["hasMany", "belongsTo", "hasOne", "hasAndBelongsToMany"]:
        print(f"  {key}:")
        values = assoc.get(key, []) or []
        if values:
            for v in values:
                print(f"    - {v}")
        else:
            print("    (none)")

    print("\nInsights:")
    for i in result.get("insights", []):
        print(f"  • {i}")

    print("\n" + "=" * 60 + "\n")


def print_entity_model(entity_model):

    if not isinstance(entity_model, dict) or not entity_model:
        print("No entities found")
        return

    print("\n" + "=" * 60)
    print("ENTITY MODEL")
    print("=" * 60)

    for entity_name, data in entity_model.items():

        print(f"\nEntity: {entity_name}")

        print("\n  Methods:")
        for m in data.get("methods", []):
            print(f"    - {m}")

        print("\n  Dependencies:")
        for d in data.get("dependencies", []):
            print(f"    - {d}")

        print("\n  Associations:")
        assoc = data.get("associations", {}) or {}

        for assoc_type in ["hasMany", "belongsTo", "hasOne", "hasAndBelongsToMany"]:
            print(f"\n    {assoc_type}:")
            values = assoc.get(assoc_type, []) or []
            if values:
                for v in values:
                    print(f"      - {v}")
            else:
                print("      (none)")

        print("\n" + "-" * 60)