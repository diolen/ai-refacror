from analysis.core.prompt_builder.blocks.base_block import BaseBlock


class ArchitectureBlock(BaseBlock):

    TITLE = "ARCHITECTURAL INSIGHTS"

    def render(self, context_data):

        insights = context_data.get(
            "insights",
            []
        )

        if not insights:
            return ""

        lines = [self.TITLE + ":"]

        for insight in insights:
            lines.append(f"  • {insight}")

        return "\n".join(lines)