import re

from memory.db import (
    save_memory,
    memory_exists
)


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


def scan_dependencies(file_path):
    with open(file_path, "r") as f:
        code = f.read()

    matches = re.findall(
        r"\$this->([A-Z][A-Za-z0-9_]+)->",
        code
    )

    dependencies = []

    for m in sorted(set(matches)):

        dependencies.append({
            "name": m,
            "type": classify_dependency(m)
        })

    return {
        "file": file_path,
        "dependencies": dependencies
    }


def extract_patterns(scan_result):

    models = [
        d["name"]
        for d in scan_result["dependencies"]
        if d["type"] == "model"
    ]

    patterns = []

    if len(models) >= 2:

        pattern = {
            "type": "pattern",
            "text": (
                "Models used together: "
                + ", ".join(sorted(models))
            ),
            "confidence": 0.7
        }

        patterns.append(pattern)

    return patterns


def save_patterns(patterns):

    for p in patterns:

        exists = memory_exists(
            p["text"],
            p["type"]
        )

        if not exists:

            save_memory(p)

            print(f"Saved: {p['text']}")

        else:

            print(f"Skipped duplicate: {p['text']}")