import re


KNOWN_COMPONENTS = {
    "Auth",
    "Session",
    "Cookie",
    "RequestHandler",
    "Paginator",
    "Security",
    "Flash",
    "Request",
    "Response"
}

METHOD_CALL_PATTERN = re.compile(
    r"\$this->([A-Z][A-Za-z0-9_]*)->([a-zA-Z0-9_]*)\("
)


def classify_model(name):
    if name in KNOWN_COMPONENTS:
        return "component"
    return "model"


def normalize_name(name):
    if not isinstance(name, str):
        return None
    name = name.strip()
    return name if name else None


def build_graph(file_path):

    with open(file_path, "r") as f:
        code = f.read()

    matches = METHOD_CALL_PATTERN.findall(code)

    graph = {
        "domain": {},
        "framework": {}
    }

    for model, method in matches:

        model = normalize_name(model)
        method = normalize_name(method)

        if not model or not method:
            continue

        category = classify_model(model)

        target = graph["framework"] if category == "component" else graph["domain"]

        if model not in target:
            target[model] = []

        if method not in target[model]:
            target[model].append(method)

    return graph