import json


def render_prompt(contract_output):

    """
    Converts structured contract → LLM-safe prompt string
    """

    return json.dumps(contract_output, indent=2, ensure_ascii=False)