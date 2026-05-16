from analysis.core.prompt_builder.compiler import PromptCompiler
from analysis.core.prompt_builder.enums import TaskType
from analysis.core.prompt_builder.prompt_context import PromptContext


def build_mock_entity_model():

    return {
        "User": {
            "methods": ["find", "save", "delete", "customBusinessLogic"],
            "dependencies": ["DB", "Cache"],
            "associations": {
                "hasMany": ["Order"],
                "belongsTo": ["Group"]
            }
        }
    }


def test_debug_compiler():

    print("\n[TEST] DEBUG COMPILER")

    entity_model = build_mock_entity_model()
    context = PromptContext()

    compiler = PromptCompiler(entity_model, context)

    output = compiler.compile(
        task_type=TaskType.DEBUG,
        target_entity="User",
        task_description="Fix recursive loading"
    )

    assert isinstance(output, str)
    assert "task type" in output.lower()
    assert "debug" in output.lower()
    assert "target entity" in output.lower()
    assert "output requirements" in output.lower()

    print("[PASS] DEBUG COMPILER")


def test_refactor_compiler():

    print("\n[TEST] REFACTOR COMPILER")

    entity_model = build_mock_entity_model()
    context = PromptContext()

    compiler = PromptCompiler(entity_model, context)

    output = compiler.compile(
        task_type=TaskType.REFACTOR,
        target_entity="User"
    )

    assert "refactor" in output.lower()
    assert "dependencies" in output.lower()

    print("[PASS] REFACTOR COMPILER")


def test_feature_compiler():

    print("\n[TEST] FEATURE COMPILER")

    entity_model = build_mock_entity_model()
    context = PromptContext()

    compiler = PromptCompiler(entity_model, context)

    output = compiler.compile(
        task_type=TaskType.FEATURE,
        target_entity="User"
    )

    assert "feature" in output.lower()
    assert "output requirements" in output.lower()

    print("[PASS] FEATURE COMPILER")


def run_all_tests():

    print("\n===================================")
    print("PROMPT COMPILER SMOKE TESTS")
    print("===================================\n")

    test_debug_compiler()
    test_refactor_compiler()
    test_feature_compiler()

    print("\n===================================")
    print("ALL TESTS PASSED")
    print("===================================\n")


if __name__ == "__main__":

    try:
        run_all_tests()

    except AssertionError as e:
        print("\n[FAIL] AssertionError:", str(e))
        raise

    except Exception as e:
        print("\n[ERROR] Unexpected error:", str(e))
        raise