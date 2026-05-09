class PromptContract:
    """
    Base abstraction for all LLM prompts.
    """

    def __init__(self, entity_model, context=None):
        self.entity_model = entity_model
        self.context = context or {}

    def build(self):
        raise NotImplementedError