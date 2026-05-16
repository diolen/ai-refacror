from analysis.core.prompt_builder.blocks.base_block import BaseBlock


class SystemRulesBlock(BaseBlock):

    TITLE = "EXECUTION RULES"

    def render(self, context_data):

        rules = context_data.get(
            "strategy_rules",
            []
        )

        if not rules:
            return ""

        lines = [self.TITLE + ":"]

        for rule in rules:
            lines.append(f"  - {rule}")

        return "\n".join(lines)