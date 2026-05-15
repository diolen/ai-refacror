from analysis.core.prompt_builder.base_contract import PromptContract


class EntityPrompt(PromptContract):
    """
    Builds structured entity-level prompt for LLM analysis.
    Stateless and deterministic.
    """

    def build(self):

        entity_model = self.entity_model or {}

        return {
            "task": "entity_analysis",
            "input": {
                "entities": self._build_entities(entity_model),
                "meta": {
                    "total_entities": len(entity_model)
                }
            }
        }

    def _build_entities(self, entity_model):

        result = []

        for name in sorted(entity_model.keys()):

            data = entity_model.get(name, {}) or {}

            result.append({
                "entity": name,
                "methods": data.get("methods", []) or [],
                "dependencies": data.get("dependencies", []) or [],
                "associations": data.get("associations", {}) or {}
            })

        return result