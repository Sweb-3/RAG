import requests

def call_llm(prompt):
    response = requests.post(
        "http://ollama:11434/api/generate",
        json={
            "model": "llama3",
            "prompt": prompt,
            "stream": False
        }
    )
    return response.json()["response"]