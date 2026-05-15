import subprocess
import sys
import time
import json


FIXTURE = "tests/fixtures/cakephp2"

CONTROLLER = f"{FIXTURE}/Controller/UsersController.php"
MODEL = f"{FIXTURE}/Model/User.php"


# -------------------------
# RUNNER
# -------------------------
def run(cmd):
    start = time.time()

    result = subprocess.run(
        cmd,
        shell=True,
        capture_output=True,
        text=True
    )

    duration = round(time.time() - start, 3)

    return result.returncode, result.stdout.strip(), result.stderr.strip(), duration


# -------------------------
# JSON PARSER
# -------------------------
def try_json(out):
    try:
        return json.loads(out)
    except Exception:
        return None


# -------------------------
# NORMALIZATION
# -------------------------
def extract_entities(data):
    if not data:
        return []

    if isinstance(data, dict):
        if "entities" in data:
            return [e.get("name") for e in data["entities"] if isinstance(e, dict)]

        if "data" in data and isinstance(data["data"], dict):
            return extract_entities(data["data"])

        if "entity" in data:
            return [data["entity"]]

    if isinstance(data, list):
        return [e.get("name") for e in data if isinstance(e, dict)]

    return []


# -------------------------
# SCAN ASSERT
# -------------------------
def assert_scan(out):
    data = try_json(out)
    entities = extract_entities(data)

    if entities:
        return "User" in entities

    return "user" in out.lower()


# -------------------------
# IMPACT ASSERT
# -------------------------
def assert_impact(out):
    data = try_json(out)

    if isinstance(data, dict):
        impact = data.get("impact", {})

        return (
            "score" in impact
            or "connectivity" in impact
            or "impact" in data
        )

    return "impact" in out.lower()


# -------------------------
# PROMPT ASSERT
# -------------------------
def assert_prompt(out):
    data = try_json(out)

    if isinstance(data, dict):
        return data.get("entity") == "User" or "User" in str(data)

    return "user" in out.lower()


# -------------------------
# MERGE ASSERT
# -------------------------
def assert_merge(out):
    data = try_json(out)

    if isinstance(data, dict):
        return (
            data.get("merged") is True
            or "diff" in data
            or "before" in data
            or "after" in data
        )

    return "merge" in out.lower() or "diff" in out.lower()


# -------------------------
# FIXED MERGE COMMAND
# -------------------------
def resolve_merge_command():
    return f"python cli.py merge {CONTROLLER} {MODEL}"


# -------------------------
# TESTS (UPDATED FOR STATELESS SYSTEM)
# -------------------------
TESTS = [

    {
        "name": "Stage 1 - Scan Pipeline",
        "command": f"python cli.py scan {CONTROLLER}",
        "assert": assert_scan
    },

    {
        "name": "Stage 2 - Impact Engine",
        "command": f"python cli.py impact User {CONTROLLER} {MODEL}",
        "assert": assert_impact
    },

    {
        "name": "Stage 3 - Prompt Builder",
        "command": f"python cli.py prompt User {CONTROLLER} {MODEL}",
        "assert": assert_prompt
    },

    {
        "name": "Stage 4 - Merge System (FIXED)",
        "command": resolve_merge_command,
        "assert": assert_merge
    }
]


# -------------------------
# RESULT
# -------------------------
class Result:
    def __init__(self, name, ok, duration, error=None):
        self.name = name
        self.ok = ok
        self.duration = duration
        self.error = error


# -------------------------
# RUN TEST
# -------------------------
def run_test(test):
    print("\n" + "=" * 60)
    print(f"RUNNING: {test['name']}")
    print("=" * 60)

    cmd = test["command"]
    cmd = cmd() if callable(cmd) else cmd

    code, out, err, duration = run(cmd)

    if code != 0:
        print("[FAIL] Command crashed")
        print(err)
        return Result(test["name"], False, duration, err)

    try:
        ok = test["assert"](out)
    except Exception as e:
        print("[FAIL] Assertion crashed")
        print(str(e))
        return Result(test["name"], False, duration, str(e))

    if not ok:
        print("[FAIL] Assertion failed")
        return Result(test["name"], False, duration, "assertion_failed")

    print(f"[PASS] ({duration}s)")
    return Result(test["name"], True, duration)


# -------------------------
# MAIN
# -------------------------
def main():
    results = []

    for t in TESTS:
        results.append(run_test(t))

    print("\n" + "#" * 60)
    print("SYSTEM VALIDATION SUMMARY")
    print("#" * 60)

    passed = 0
    failed = 0

    for r in results:
        status = "PASS" if r.ok else "FAIL"
        print(f"[{status}] {r.name} ({r.duration}s)")

        if not r.ok:
            print(f"       ERROR: {r.error}")
            failed += 1
        else:
            passed += 1

    print("\n" + "-" * 60)
    print(f"PASSED: {passed}")
    print(f"FAILED: {failed}")
    print("-" * 60)

    if failed > 0:
        sys.exit(1)

    print("\nALL SYSTEM VALIDATIONS PASSED")


if __name__ == "__main__":
    main()