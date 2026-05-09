import re
from collections import defaultdict


KNOWN_COMPONENTS = {
    "Auth",
    "Session",
    "Cookie",
    "RequestHandler",
    "Paginator",
    "Security"
}

KNOWN_HELPERS = {
    "Html",
    "Form",
    "Js",
    "Time"
}


def classify_dependency(name):

    if name in KNOWN_COMPONENTS:
        return "component"

    if name in KNOWN_HELPERS:
        return "helper"

    return "model"


# =========================
# SCAN
# =========================
def scan_dependencies(file_path):

    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
        code = f.read()

    matches = re.findall(
        r"\$this->([A-Z][A-Za-z0-9_]+)->([a-zA-Z0-9_]+)\(",
        code
    )

    freq = defaultdict(int)

    for model, method in matches:
        freq[(model, method)] += 1

    dependencies = []

    for (model, method), count in freq.items():
        dependencies.append({
            "name": model,
            "method": method,
            "frequency": count
        })

    return {
        "file": file_path,
        "dependencies": dependencies
    }