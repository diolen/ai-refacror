from analysis.core.impact_engine import compute_entity_impact
from memory.db import save_milestone, save_decision, save_insight


MILESTONE_FREQUENCY_THRESHOLD = 3


# =========================
# MAIN PIPELINE
# =========================
def enrich_entity_model(entity_model, scan_result, method_graph):
    if not isinstance(entity_model, dict):
        return {}

    dependencies = _collect_dependency_entries(scan_result)
    method_events = _collect_method_events(method_graph)

    enriched = {}

    for entity_name, entity_data in entity_model.items():
        if not isinstance(entity_data, dict):
            continue

        impact = compute_entity_impact(entity_name, entity_model) or {}

        timeline = _build_timeline(entity_name, dependencies, method_events)
        milestones = _build_milestones(entity_name, dependencies)
        decisions = _build_decisions(entity_name, entity_data, method_graph)
        insights = _build_insights(impact)
        patterns = _build_patterns(entity_name, dependencies, method_events)

        # =========================
        # PERSIST MEMORY
        # =========================
        for m in milestones:
            save_milestone(m)

        for d in decisions:
            save_decision(d)

        for i in insights:
            save_insight(i)

        enriched[entity_name] = {
            "methods": entity_data.get("methods", []),
            "dependencies": entity_data.get("dependencies", []),
            "associations": entity_data.get("associations", {}),
            "timeline": timeline,
            "milestones": milestones,
            "decisions": decisions,
            "insights": insights,
            "patterns": patterns,
        }

    return enriched


# =========================
# DEPENDENCY EXTRACTION
# =========================
def _collect_dependency_entries(scan_result):
    if not isinstance(scan_result, dict):
        return []

    dependencies = scan_result.get("dependencies", [])
    if not isinstance(dependencies, list):
        return []

    entries = []

    for item in dependencies:
        if not isinstance(item, dict):
            continue

        model = item.get("name")
        method = item.get("method")
        frequency = item.get("frequency", 1)

        if not isinstance(model, str) or not model.strip():
            continue
        if not isinstance(method, str) or not method.strip():
            continue
        if not isinstance(frequency, int) or frequency < 1:
            frequency = 1

        entries.append({
            "entity": model.strip(),
            "method": method.strip(),
            "frequency": frequency,
        })

    return entries


# =========================
# METHOD GRAPH EVENTS
# =========================
def _collect_method_events(method_graph):
    if not isinstance(method_graph, dict):
        return {}

    events = {}

    for section_data in method_graph.values():
        if not isinstance(section_data, dict):
            continue

        for entity_name, methods in section_data.items():
            if not isinstance(entity_name, str):
                continue
            if not isinstance(methods, list):
                continue

            for method in methods:
                if not isinstance(method, str) or not method.strip():
                    continue

                events.setdefault(entity_name, []).append(method.strip())

    return events


# =========================
# TIMELINE
# =========================
def _build_timeline(entity_name, dependency_entries, method_events):
    timeline = []
    seen = {}

    for item in dependency_entries:
        if item["entity"] != entity_name:
            continue

        event = f"{item['entity']}.{item['method']}"
        seen[event] = seen.get(event, 0) + item["frequency"]

    for method in method_events.get(entity_name, []):
        event = f"{entity_name}.{method}"
        seen[event] = seen.get(event, 0) + 1

    for event, count in seen.items():
        timeline.append({"event": event, "count": count})

    return sorted(timeline, key=lambda e: (-e["count"], e["event"]))


# =========================
# MILESTONES
# =========================
def _build_milestones(entity_name, dependency_entries):
    milestones = []

    entity_dependencies = [
        item for item in dependency_entries if item["entity"] == entity_name
    ]

    if entity_dependencies:
        milestones.append(f"{entity_name} reached active dependency usage")

    total = sum(item["frequency"] for item in entity_dependencies)

    if total >= MILESTONE_FREQUENCY_THRESHOLD:
        milestones.append(f"{entity_name} reached stable usage")

    per_method = {}
    for item in entity_dependencies:
        per_method[item["method"]] = per_method.get(item["method"], 0) + item["frequency"]

    dominant = None
    dominant_count = 0

    for method, count in per_method.items():
        if count > dominant_count:
            dominant = method
            dominant_count = count

    if dominant and dominant_count >= MILESTONE_FREQUENCY_THRESHOLD:
        milestones.append(f"{entity_name}.{dominant} became dominant dependency")

    return milestones


# =========================
# DECISIONS
# =========================
def _build_decisions(entity_name, entity_data, method_graph):
    decisions = []

    if isinstance(method_graph, dict) and "framework" in method_graph:
        decisions.append("Filtered framework entities from domain graph")

    dependencies = entity_data.get("dependencies", [])

    if isinstance(dependencies, list) and entity_name not in dependencies:
        decisions.append("Normalized self-references in dependencies")

    return decisions


# =========================
# INSIGHTS
# =========================
def _build_insights(impact):
    score = impact.get("score", 0)
    connectivity = impact.get("connectivity", 0)

    complexity = "low"
    if score >= 18:
        complexity = "high"
    elif score >= 10:
        complexity = "medium"

    coupling = "low"
    if connectivity >= 5:
        coupling = "high"
    elif connectivity >= 3:
        coupling = "medium"

    return [
        f"complexity: {complexity}",
        f"coupling: {coupling}",
    ]


# =========================
# PATTERNS
# =========================
def _build_patterns(entity_name, dependency_entries, method_events):
    patterns = []

    repeated = {}

    for item in dependency_entries:
        if item["entity"] != entity_name:
            continue

        if item["frequency"] > 1:
            repeated[item["method"]] = repeated.get(item["method"], 0) + item["frequency"]

    for method, count in sorted(repeated.items(), key=lambda x: (-x[1], x[0])):
        patterns.append(f"Repeated method call: {entity_name}.{method} ({count})")

    occurrences = {}

    for method in method_events.get(entity_name, []):
        occurrences[method] = occurrences.get(method, 0) + 1

    for method, count in sorted(occurrences.items(), key=lambda x: (-x[1], x[0])):
        if count > 1:
            patterns.append(f"Repeated dependency usage: {entity_name}.{method} ({count})")

    return patterns