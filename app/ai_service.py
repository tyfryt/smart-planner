import requests
import json
import re

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "mistral"


def ask_ollama(prompt: str) -> str:
    """
    Базовый запрос к Ollama
    """
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
        data = response.json()

        return data.get("response", "").strip()

    except Exception as e:
        print(f"Ollama error: {e}")
        return ""


# ---------------------------
# CATEGORY
# ---------------------------

def get_category(task: str) -> str:
    prompt = f"""
Ты классификатор задач.

Выбери ОДНУ категорию строго из списка:
- работа
- личное
- здоровье
- обучение
- другое

Правила:
- отвечай только одним словом
- без объяснений
- без знаков препинания
- без markdown

Задача: "{task}"

Категория:
"""

    result = ask_ollama(prompt).lower().strip()

    allowed = {"работа", "личное", "здоровье", "обучение", "другое"}

    # чистим мусор (если модель болтает)
    result = re.sub(r"[^a-zа-яё]", "", result)

    return result if result in allowed else "другое"


# ---------------------------
# ESTIMATE TIME
# ---------------------------

def estimate_time(task: str) -> int:
    prompt = f"""
Ты ассистент по оценке времени задач.

Верни ТОЛЬКО число минут.

Правила:
- только число
- без текста
- без объяснений
- округляй до 5-10 минут
- если не уверен → 30

Примеры:
- "помыть посуду" → 10
- "написать письмо" → 20
- "учёба 1 час" → 60

Задача: "{task}"

Минуты:
"""

    result = ask_ollama(prompt)

    # вытаскиваем первое число
    match = re.search(r"\d+", result)

    if match:
        return int(match.group())

    return 30


# ---------------------------
# COMBINED ANALYSIS (лучший вариант)
# ---------------------------

def analyze_task(task: str) -> dict:
    """
    Один запрос вместо двух — быстрее и стабильнее
    """

    prompt = f"""
Ты анализатор задач.

Верни СТРОГО JSON:

{{
  "category": "работа|личное|здоровье|обучение|другое",
  "estimated_time": number
}}

Правила:
- только JSON
- без текста
- без markdown
- без пояснений
- category строго из списка

Задача: "{task}"
"""

    response = ask_ollama(prompt)

    try:
        data = json.loads(response)

        category = data.get("category", "другое").lower()
        time = int(data.get("estimated_time", 30))

        allowed = {"работа", "личное", "здоровье", "обучение", "другое"}

        if category not in allowed:
            category = "другое"

        return {
            "category": category,
            "estimated_time": time
        }

    except Exception:
        return {
            "category": "другое",
            "estimated_time": 30
        }