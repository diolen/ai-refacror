class PromptContext:
    """
    Shared context container for prompt building pipeline.
    """

    def __init__(self):
        self.data = {
            "impact_score": None,
            "connectivity": None,
            "insights": [],
            "risk_score": None
        }

    # =========================
    # UPDATE CONTEXT
    # =========================
    def update(self, **kwargs):
        for k, v in kwargs.items():
            self.data[k] = v

    # =========================
    # SAFE GET
    # =========================
    def get(self, key=None, default=None):

        if key is None:
            return self.data

        return self.data.get(key, default)

    # =========================
    # RESET CONTEXT
    # =========================
    def reset(self):
        self.data = {
            "impact_score": None,
            "connectivity": None,
            "insights": [],
            "risk_score": None
        }