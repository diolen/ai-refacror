from analysis.core.prompt_builder.base_contract import PromptContract


class RefactorPrompt(PromptContract):

    def build(self, target_entity):

        entity = self.entity_model.get(target_entity)

        return {
            "task": "refactor_suggestion",
            "target": target_entity,
            "input": {
                "methods": entity.get("methods", []),
                "dependencies": entity.get("dependencies", []),
                "associations": entity.get("associations", {}),
                "insights": self.context.get("insights", []),
                "risk_score": self.context.get("risk_score")
            }
        }