class PromptContext:

    def __init__(self):

        self.data = {
            "impact_score": None,
            "connectivity": None,
            "insights": [],
            "risk_score": None
        }

    def update(self, **kwargs):

        for k, v in kwargs.items():
            self.data[k] = v

    def get(self):
        return self.data