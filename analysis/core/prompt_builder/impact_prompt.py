from analysis.core.prompt_builder.base_contract import PromptContract


class ImpactPrompt(PromptContract):
    """
    Builds deterministic impact analysis prompt.

    Uses only current entity state + computed metrics.
    No historical or persistence-based fields allowed.
    """

    def build(self, target_entity):

        entity = (self.entity_model or {}).get(target_entity)

        # =========================
        # SAFETY LAYER
        # =========================
        if not isinstance(entity, dict):
            entity = {
                "methods": [],
                "dependencies": [],
                "associations": {}
            }

        return {
            "task": "impact_analysis",
            "target": target_entity,

            "input": {
                # =========================
                # CORE ENTITY (CURRENT STATE ONLY)
                # =========================
                "entity": {
                    "methods": entity.get("methods", []) or [],
                    "dependencies": entity.get("dependencies", []) or [],
                    "associations": entity.get("associations", {}) or {}
                },

                # =========================
                # METRICS (CURRENT RUN ONLY)
                # =========================
                "metrics": {
                    "impact_score": self.context.get("impact_score", 0),
                    "connectivity": self.context.get("connectivity", 0)
                },

                # =========================
                # INSIGHTS (CURRENT RUN ONLY)
                # =========================
                "insights": self.context.get("insights", [])
            }
        }