from analysis.core.prompt_builder.strategies.base_strategy import BaseStrategy


class FeatureStrategy(BaseStrategy):

    PRIORITY_FIELDS = [
        "associations",
        "dependencies",
        "methods"
    ]

    MAX_INSIGHTS = 4

    def process(self, context_data):

        entity = context_data.get("entity", {})

        prioritized_entity = {
            "methods": entity.get("methods", [])[:20],
            "dependencies": entity.get("dependencies", []),
            "associations": entity.get("associations", {})
        }

        insights = []

        for insight in context_data.get(
            "insights",
            []
        ):

            if (
                "domain" in insight.lower()
                or "aggregation" in insight.lower()
                or "logic" in insight.lower()
            ):
                insights.append(insight)

        context_data["entity"] = prioritized_entity
        context_data["insights"] = insights[:self.MAX_INSIGHTS]

        context_data["strategy_name"] = "feature"

        return context_data