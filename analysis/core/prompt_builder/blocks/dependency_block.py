from analysis.core.prompt_builder.blocks.base_block import BaseBlock


class DependencyBlock(BaseBlock):

    TITLE = "DEPENDENCIES"

    def render(self, context_data):

        entity = context_data.get("entity", {})

        dependencies = entity.get(
            "dependencies",
            []
        )

        if not dependencies:
            return ""

        lines = [self.TITLE + ":"]

        for dep in dependencies:
            lines.append(f"  - {dep}")

        return "\n".join(lines)