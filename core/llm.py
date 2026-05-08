import requests
import json

OLLAMA_URL = "http://localhost:11434/v1/chat/completions"

MODEL = "kamekichi128/qwen3-4b-instruct-2507:latest"

def call_llm(prompt: str):
    payload = {
        "model": MODEL,
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }

    r = requests.post(OLLAMA_URL, json=payload)
    r.raise_for_status()

    return r.json()["choices"][0]["message"]["content"]