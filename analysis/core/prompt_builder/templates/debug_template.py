from analysis.core.prompt_builder.templates.base_template import BaseTemplate


class DebugTemplate(BaseTemplate):

    TASK_NAME = "debug"

    OBJECTIVE = (
        "Identify root cause and suggest minimal "
        "safe fix preserving current behavior."
    )

    STRATEGY_RULES = [
        "Focus on execution flow.",
        "Avoid broad refactors.",
        "Preserve existing architecture.",
        "Prefer minimal safe fixes.",
        "Validate dependency assumptions."
    ]