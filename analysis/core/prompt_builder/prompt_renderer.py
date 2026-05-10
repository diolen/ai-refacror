def render_prompt(contract_output):

    task = contract_output.get("task", "unknown")
    target = contract_output.get("target", "unknown")

    data = contract_output.get("input", {})

    lines = []

    # =========================
    # HEADER
    # =========================
    lines.append(f"TASK: {task}")
    lines.append(f"TARGET: {target}")

    # =========================
    # SCORE
    # =========================
    if data.get("score") is not None:
        lines.append(f"\nIMPACT SCORE: {data['score']}")

    if data.get("connectivity") is not None:
        lines.append(f"CONNECTIVITY: {data['connectivity']}")

    # =========================
    # ENTITY CORE
    # =========================
    entity = data.get("entity", {})

    if isinstance(entity, dict):

        methods = entity.get("methods", [])
        if methods:
            lines.append("\nMETHODS:")
            for m in methods:
                lines.append(f"  - {m}")

        dependencies = entity.get("dependencies", [])
        if dependencies:
            lines.append("\nDEPENDENCIES:")
            for d in dependencies:
                lines.append(f"  - {d}")

        associations = entity.get("associations", {})
        if associations:
            lines.append("\nASSOCIATIONS:")
            for assoc_type, values in associations.items():
                if values:
                    lines.append(f"  {assoc_type}:")
                    for v in values:
                        lines.append(f"    - {v}")

    # =========================
    # TIMELINE (FIXED)
    # =========================
    timeline = data.get("timeline", [])
    if timeline:
        lines.append("\nTIMELINE:")
        for t in timeline:
            lines.append(f"  - {t.get('event')} ({t.get('count')})")

    # =========================
    # PATTERNS (FIXED)
    # =========================
    patterns = data.get("patterns", [])
    if patterns:
        lines.append("\nPATTERNS:")
        for p in patterns:
            lines.append(f"  • {p}")

    # =========================
    # MILESTONES (FIXED)
    # =========================
    milestones = data.get("milestones", [])
    if milestones:
        lines.append("\nMILESTONES:")
        for m in milestones:
            lines.append(f"  • {m}")

    # =========================
    # DECISIONS (FIXED)
    # =========================
    decisions = data.get("decisions", [])
    if decisions:
        lines.append("\nDECISIONS:")
        for d in decisions:
            lines.append(f"  • {d}")

    # =========================
    # INSIGHTS
    # =========================
    insights = data.get("insights", [])
    if insights:
        lines.append("\nARCHITECTURAL INSIGHTS:")
        for i in insights:
            lines.append(f"  • {i}")

    # =========================
    # OBJECTIVE
    # =========================
    if task == "impact_analysis":
        lines.append("\nOBJECTIVE:")
        lines.append("Analyze architectural impact and propagation risk.")

    elif task == "refactor_suggestion":
        lines.append("\nOBJECTIVE:")
        lines.append("Suggest safe refactor strategy preserving business behavior.")

    return "\n".join(lines)