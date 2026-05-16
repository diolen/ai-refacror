from analysis.core.prompt_builder.blocks.base_block import BaseBlock


class OutputBlock(BaseBlock):

    TITLE = "OUTPUT REQUIREMENTS"

    def render(self, context_data):

        task = context_data.get("task")

        lines = [self.TITLE + ":"]

        if task == "debug":

            lines.append(
                "- Explain root cause."
            )

            lines.append(
                "- Suggest minimal safe fix."
            )

            lines.append(
                "- Avoid speculative refactors."
            )

        elif task == "feature":

            lines.append(
                "- Reuse existing architecture."
            )

            lines.append(
                "- Explain integration points."
            )

            lines.append(
                "- Preserve framework conventions."
            )

        else:

            lines.append(
                "- Preserve public interfaces."
            )

            lines.append(
                "- Suggest incremental refactor."
            )

            lines.append(
                "- Avoid behavioral regressions."
            )

        return "\n".join(lines)