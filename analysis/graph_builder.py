import re


KNOWN_COMPONENTS = {
    "Auth",
    "Session",
    "Cookie",
    "RequestHandler",
    "Paginator",
    "Security"
}


METHOD_CALL_PATTERN = re.compile(
    r"\$this->([A-Z][A-Za-z0-9_]+)->([a-zA-Z0-9_]+)\("
)


def build_graph(file_path):

    with open(file_path, "r") as f:
        code = f.read()

    matches = METHOD_CALL_PATTERN.findall(code)

    graph = {}

    for model, method in matches:

        if model in KNOWN_COMPONENTS:
            continue

        if model not in graph:
            graph[model] = []

        if method not in graph[model]:
            graph[model].append(method)

    return graph