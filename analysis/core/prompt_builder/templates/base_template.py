from analysis.core.prompt_builder.base_contract import PromptContract


class BaseTemplate(PromptContract):

    TASK_NAME = "generic"

    OBJECTIVE = "Analyze entity."

    STRATEGY_RULES = []

    def build(
        self,
        target_entity,
        task_description=""
    ):

        entity = self.entity_model.get(target_entity, {})

        return {
            "task": self.TASK_NAME,
            "target": target_entity,
            "task_description": task_description,
            "input": {
                "entity": entity,
                "metrics": {
                    "impact_score": self.context.get("impact_score"),
                    "connectivity": self.context.get("connectivity"),
                    "risk_score": self.context.get("risk_score")
                },
                "insights": self.context.get("insights", []),
                "strategy_rules": self.STRATEGY_RULES,
                "objective": self.OBJECTIVE
            }
        }