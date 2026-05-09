from analysis.core.prompt_builder.base_contract import PromptContract


class ImpactPrompt(PromptContract):

    def build(self, target_entity):

        entity = self.entity_model.get(target_entity)

        return {
            "task": "impact_analysis",
            "target": target_entity,
            "input": {
                "entity": entity,
                "score": self.context.get("impact_score"),
                "connectivity": self.context.get("connectivity"),
                "insights": self.context.get("insights", []),
                "dependencies": entity.get("dependencies", []),
                "associations": entity.get("associations", {})
            }
        }