from analysis.core.prompt_builder.templates.base_template import BaseTemplate


class RefactorTemplate(BaseTemplate):

    TASK_NAME = "refactor"

    OBJECTIVE = (
        "Suggest safe refactor strategy preserving "
        "business behavior and public interfaces."
    )

    STRATEGY_RULES = [
        "Preserve public APIs.",
        "Avoid unnecessary architectural rewrites.",
        "Prefer incremental extraction.",
        "Avoid breaking changes.",
        "Respect CakePHP legacy conventions."
    ]