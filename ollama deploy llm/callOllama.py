import requests

def call_ollama(prompt, model="deepseek-r1:7b"):
    url = "http://localhost:11434/api/generate"
    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False
    }
    response = requests.post(url, json=payload)
    response.raise_for_status()
    result = response.json()
    return result.get("response", "")

if __name__ == "__main__":
    prompt = "你好，介绍一下你自己。"
    answer = call_ollama(prompt)
    print("Ollama回复：", answer)