from analysis.core.prompt_builder.strategies.base_strategy import BaseStrategy


class DebugStrategy(BaseStrategy):

    PRIORITY_FIELDS = [
        "dependencies",
        "associations",
        "methods"
    ]

    MAX_INSIGHTS = 8

    def process(self, context_data):

        entity = context_data.get("entity", {})

        prioritized_entity = {
            "methods": entity.get("methods", []),
            "dependencies": entity.get("dependencies", []),
            "associations": entity.get("associations", {})
        }

        insights = context_data.get(
            "insights",
            []
        )[:self.MAX_INSIGHTS]

        context_data["entity"] = prioritized_entity
        context_data["insights"] = insights

        context_data["strategy_name"] = "debug"

        return context_data