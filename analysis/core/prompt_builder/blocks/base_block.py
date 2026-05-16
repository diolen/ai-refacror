class BaseBlock:

    TITLE = None

    def render(self, context_data):

        raise NotImplementedError