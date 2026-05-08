import re

def extract_function(file_path, function_name):
    with open(file_path, "r") as f:
        code = f.read()

    pattern = rf"(public|protected|private)?\s*function\s+{function_name}\s*\([^)]*\)\s*\{{"

    match = re.search(pattern, code)

    if not match:
        raise Exception(f"Function not found: {function_name}")

    start = match.start()

    brace = 0
    end = None

    for i in range(start, len(code)):
        if code[i] == "{":
            brace += 1
        elif code[i] == "}":
            brace -= 1
            if brace == 0:
                end = i
                break

    if end is None:
        raise Exception("Could not parse function body")

    print("Searching for:", function_name)
    print("File loaded OK")

    return code[start:end+1]
