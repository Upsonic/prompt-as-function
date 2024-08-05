OPENAI_API_KEY = None


class Configs:
    def __init__(self):
        self.OPENAI_API_KEY = None



prompt_as_config = Configs()


def OPENAI_API_KEY():
    return prompt_as_config.OPENAI_API_KEY