import re
import os

ASSOCIATION_TYPES = [
    "belongsTo",
    "hasMany",
    "hasOne",
    "hasAndBelongsToMany"
]


def normalize_model_name(file_path):
    return os.path.splitext(os.path.basename(file_path))[0].strip()


def parse_associations(file_path):

    with open(file_path, "r") as f:
        code = f.read()

    model_name = normalize_model_name(file_path)

    result = {
        "model": model_name,
        "associations": {
            "belongsTo": [],
            "hasMany": [],
            "hasOne": [],
            "hasAndBelongsToMany": []
        }
    }

    for assoc_type in ASSOCIATION_TYPES:

        pattern = (
            r"public\s+\$"
            + assoc_type +
            r"\s*=\s*array\s*\((.*?)\);"
        )

        matches = re.findall(pattern, code, re.DOTALL)

        models = set()

        for block in matches:
            found = re.findall(r"'([A-Z][A-Za-z0-9_]*)'", block)
            for f in found:
                if isinstance(f, str) and f.strip():
                    models.add(f.strip())

        result["associations"][assoc_type] = sorted(models)

    return result