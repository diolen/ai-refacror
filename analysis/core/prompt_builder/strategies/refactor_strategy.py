from analysis.core.prompt_builder.strategies.base_strategy import BaseStrategy


class RefactorStrategy(BaseStrategy):

    PRIORITY_FIELDS = [
        "methods",
        "dependencies",
        "associations"
    ]

    MAX_INSIGHTS = 5

    def process(self, context_data):

        entity = context_data.get("entity", {})

        prioritized_entity = {
            "methods": entity.get("methods", []),
            "dependencies": entity.get("dependencies", []),
            "associations": entity.get("associations", {})
        }

        insights = []

        for insight in context_data.get(
            "insights",
            []
        ):

            if (
                "risk" in insight.lower()
                or "coupling" in insight.lower()
                or "connected" in insight.lower()
            ):
                insights.append(insight)

        context_data["entity"] = prioritized_entity
        context_data["insights"] = insights[:self.MAX_INSIGHTS]

        context_data["strategy_name"] = "refactor"

        return context_data