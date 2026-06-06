import requests
import json
import re

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "mistral"

def ask_ollama(prompt: str) -> str:
    try:
        response = requests.post(
            OLLAMA_URL,
            json={
                "model": MODEL,
                "prompt": prompt,
                "stream": False
            },
            timeout=30
        )
        response.raise_for_status()
        return response.json().get("response", "").strip()
    except Exception as e:
        print(f"Ollama error: {e}")
        return ""


def analyze_task(task: str) -> dict:
    prompt = f"""
Ты анализатор задач. Верни СТРОГО JSON:
{{ "category": "работа|личное|здоровье|обучение|другое", "estimated_time": number }}
Задача: "{task}"
"""
    response = ask_ollama(prompt)
    try:
        # Извлекаем JSON из ответа Ollama
        import json, re
        match = re.search(r'\{.*?\}', response, re.DOTALL)
        return json.loads(match.group(0))
    except:
        # Резервный вариант, если ИИ ошибся в формате
        return {"category": "другое", "estimated_time": 30}