from analysis.core.prompt_builder.base_contract import PromptContract


class EntityPrompt(PromptContract):

    def build(self):

        return {
            "task": "entity_analysis",
            "input": {
                "entities": self._build_entities(),
                "meta": {
                    "total_entities": len(self.entity_model)
                }
            }
        }

    def _build_entities(self):

        result = []

        for name, data in self.entity_model.items():

            result.append({
                "entity": name,
                "methods": data.get("methods", []),
                "dependencies": data.get("dependencies", []),
                "associations": data.get("associations", {})
            })

        return result