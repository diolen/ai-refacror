class BaseStrategy:

    PRIORITY_FIELDS = []

    MAX_INSIGHTS = 5

    def process(self, context_data):

        raise NotImplementedError