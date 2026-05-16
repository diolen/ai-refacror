from analysis.core.prompt_builder.templates.base_template import BaseTemplate


class FeatureTemplate(BaseTemplate):

    TASK_NAME = "feature"

    OBJECTIVE = (
        "Implement new functionality using existing "
        "project conventions and extension points."
    )

    STRATEGY_RULES = [
        "Reuse existing patterns when possible.",
        "Prefer additive implementation strategy.",
        "Minimize architectural disruption.",
        "Respect framework conventions.",
        "Avoid unnecessary abstractions."
    ]