from analysis.core.prompt_builder.enums import TaskType

from analysis.core.prompt_builder.templates.debug_template import DebugTemplate
from analysis.core.prompt_builder.templates.refactor_template import RefactorTemplate
from analysis.core.prompt_builder.templates.feature_template import FeatureTemplate

from analysis.core.prompt_builder.prompt_renderer import render_prompt

from analysis.core.prompt_builder.strategies.debug_strategy import DebugStrategy
from analysis.core.prompt_builder.strategies.refactor_strategy import RefactorStrategy
from analysis.core.prompt_builder.strategies.feature_strategy import FeatureStrategy


class PromptCompiler:

    def __init__(self, entity_model, context):

        self.entity_model = entity_model
        self.context = context

    # ==========================================
    # TEMPLATE FACTORY
    # ==========================================

    def _resolve_template(self, task_type):

        if task_type == TaskType.DEBUG:

            return DebugTemplate(
                self.entity_model,
                self.context
            )

        if task_type == TaskType.FEATURE:

            return FeatureTemplate(
                self.entity_model,
                self.context
            )

        return RefactorTemplate(
            self.entity_model,
            self.context
        )

    # ==========================================
    # STRATEGY FACTORY
    # ==========================================

    def _resolve_strategy(self, task_type):

        if task_type == TaskType.DEBUG:
            return DebugStrategy()

        if task_type == TaskType.FEATURE:
            return FeatureStrategy()

        return RefactorStrategy()

    # ==========================================
    # MAIN COMPILER ENTRY
    # ==========================================

    def compile(
        self,
        task_type,
        target_entity,
        task_description=""
    ):

        template = self._resolve_template(task_type)

        contract_output = template.build(
            target_entity=target_entity,
            task_description=task_description
        )

        strategy = self._resolve_strategy(task_type)

        processed_input = strategy.process(
            contract_output["input"]
        )

        contract_output["input"] = processed_input

        return render_prompt(contract_output)