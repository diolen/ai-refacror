from analysis.core.prompt_builder.base_contract import PromptContract


class ImpactPrompt(PromptContract):

    def build(self, target_entity):

        entity = self.entity_model.get(target_entity)

        # =========================
        # SAFETY LAYER (IMPORTANT FIX)
        # =========================
        if not isinstance(entity, dict):
            entity = {
                "methods": [],
                "dependencies": [],
                "associations": {},
                "milestones": [],
                "decisions": [],
                "patterns": [],
                "timeline": []
            }

        return {
            "task": "impact_analysis",
            "target": target_entity,

            "input": {
                # =========================
                # CORE ENTITY
                # =========================
                "entity": entity,

                # =========================
                # METRICS (from context)
                # =========================
                "score": self.context.get("impact_score"),
                "connectivity": self.context.get("connectivity"),

                # =========================
                # AI INSIGHTS (from context)
                # =========================
                "insights": self.context.get("insights", []),

                # =========================
                # STRUCTURE (entity_model)
                # =========================
                "methods": entity.get("methods", []),
                "dependencies": entity.get("dependencies", []),
                "associations": entity.get("associations", {}),

                # =========================
                # ENRICHED ANALYSIS LAYER
                # =========================
                "milestones": entity.get("milestones", []),
                "decisions": entity.get("decisions", []),
                "patterns": entity.get("patterns", []),
                "timeline": entity.get("timeline", [])
            }
        }