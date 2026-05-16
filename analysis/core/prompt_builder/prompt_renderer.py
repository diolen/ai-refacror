from analysis.core.prompt_builder.blocks.system_rules_block import SystemRulesBlock
from analysis.core.prompt_builder.blocks.impact_block import ImpactBlock
from analysis.core.prompt_builder.blocks.dependency_block import DependencyBlock
from analysis.core.prompt_builder.blocks.architecture_block import ArchitectureBlock
from analysis.core.prompt_builder.blocks.output_block import OutputBlock


BLOCKS = [
    SystemRulesBlock(),
    ImpactBlock(),
    DependencyBlock(),
    ArchitectureBlock(),
    OutputBlock()
]


def render_prompt(contract_output):

    task = contract_output.get("task", "unknown")
    target = contract_output.get("target", "unknown")
    task_description = contract_output.get("task_description", "")

    data = contract_output.get("input", {})

    context_data = dict(data)
    context_data["task"] = task

    lines = []

    # ==========================================
    # HEADER
    # ==========================================

    lines.append(f"TASK TYPE: {task}")
    lines.append(f"TARGET ENTITY: {target}")

    if task_description:
        lines.append(
            f"TASK DESCRIPTION: {task_description}"
        )

    # ==========================================
    # OBJECTIVE
    # ==========================================

    objective = data.get("objective")

    if objective:

        lines.append("\nOBJECTIVE:")
        lines.append(objective)

    # ==========================================
    # ENTITY METHODS
    # ==========================================

    entity = data.get("entity", {})

    methods = entity.get("methods", [])

    if methods:

        lines.append("\nMETHODS:")

        for method in methods:
            lines.append(f"  - {method}")

    # ==========================================
    # BLOCK PIPELINE
    # ==========================================

    for block in BLOCKS:

        rendered = block.render(context_data)

        if rendered:
            lines.append("\n" + rendered)

    return "\n".join(lines)