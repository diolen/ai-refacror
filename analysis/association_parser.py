import re

from memory.db import (
    save_memory,
    memory_exists
)


ASSOCIATION_TYPES = [
    "belongsTo",
    "hasMany",
    "hasOne",
    "hasAndBelongsToMany"
]


def parse_associations(file_path):

    with open(file_path, "r") as f:
        code = f.read()

    model_name = (
        file_path.split("/")[-1]
        .replace(".php", "")
    )

    result = {
        "model": model_name,
        "associations": {}
    }

    for assoc_type in ASSOCIATION_TYPES:

        pattern = (
            r"public\s+\$"
            + assoc_type
            + r"\s*=\s*array\s*\((.*?)\);"
        )

        matches = re.findall(
            pattern,
            code,
            re.DOTALL
        )

        associations = []

        for block in matches:

            models = re.findall(
                r"'([A-Z][A-Za-z0-9_]+)'",
                block
            )

            unique_models = sorted(set(models))

            associations.extend(unique_models)

        result["associations"][assoc_type] = (
            sorted(set(associations))
        )

    return result


def extract_association_patterns(result):

    patterns = []

    source_model = result["model"]

    for assoc_type, targets in (
        result["associations"].items()
    ):

        for target in targets:

            pattern = {
                "type": "association",
                "text": (
                    f"{source_model} "
                    f"{assoc_type} "
                    f"{target}"
                ),
                "confidence": 0.9
            }

            patterns.append(pattern)

    return patterns


def save_association_patterns(patterns):

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