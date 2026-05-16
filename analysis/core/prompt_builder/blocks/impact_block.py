from analysis.core.prompt_builder.blocks.base_block import BaseBlock


class ImpactBlock(BaseBlock):

    TITLE = "ARCHITECTURAL METRICS"

    def render(self, context_data):

        metrics = context_data.get("metrics", {})

        lines = [self.TITLE + ":"]

        impact_score = metrics.get("impact_score")
        connectivity = metrics.get("connectivity")
        risk_score = metrics.get("risk_score")

        if impact_score is not None:
            lines.append(
                f"  - Impact Score: {impact_score}"
            )

        if connectivity is not None:
            lines.append(
                f"  - Connectivity: {connectivity}"
            )

        if risk_score is not None:
            lines.append(
                f"  - Risk Score: {risk_score}"
            )

        return "\n".join(lines)