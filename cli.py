import sys

from core.llm import call_llm
from core.parser import extract_function
from core.patcher import replace_function

from memory.db import save_change


def run_refactor(args):
    file_path = args[0]
    function_name = args[1]
    instructions = " ".join(args[2:])

    input_code = extract_function(file_path, function_name)

    prompt = f"""
You are a PHP (CakePHP 2) code transformer.

RULES:
- do not change business logic
- return only PHP code

TASK:
{instructions}

CODE:
{input_code}
"""

    output = call_llm(prompt)

    replace_function(file_path, input_code, output)

    save_change(
        file_path=file_path,
        function=function_name,
        prompt=instructions,
        model="ollama",
        input_code=input_code,
        output_code=output,
        status="success",
        summary=instructions,
        reason="manual refactor"
    )

    print("DONE")


def run_memory(args):
    from memory.view import (
        show_last,
        search,
        show_memory,
        show_timeline
    )

    if len(args) == 0:
        show_last()

    elif args[0] == "search":
        search(args[1])

    elif args[0] == "patterns":
        show_memory()

    elif args[0] == "timeline":
        show_timeline()


def run_scan(args):
    from analysis.dependency_scan import (
        scan_dependencies,
        extract_patterns,
        save_patterns
    )

    file_path = args[0]

    result = scan_dependencies(file_path)

    print("\nDependencies:")
    for d in result["dependencies"]:
        print(f"- {d['name']} ({d['type']})")

    patterns = extract_patterns(result)

    if patterns:
        print("\nPatterns:")
        for p in patterns:
            print(f"- {p['text']}")

        save_patterns(patterns)

        print("\nPatterns saved to memory")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage:")
        print("  refactor <file> <function> <instructions>")
        print("  memory")
        print("  memory search <term>")
        print("  memory patterns")
        print("  memory timeline")
        print("  scan <file>")
        exit()

    command = sys.argv[1]

    if command == "memory":
        run_memory(sys.argv[2:])

    elif command == "scan":
        run_scan(sys.argv[2:])

    elif command == "refactor":
        run_refactor(sys.argv[2:])

    else:
        print("Unknown command")