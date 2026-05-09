import requests


OLLAMA_URL = "http://localhost:11434/api/chat"


import requests

OLLAMA_URL = "http://localhost:11434/api/generate"


def ask_ollama(prompt):
    response = requests.post(
        OLLAMA_URL,
        json={
            "model": "mistral",
            "prompt": prompt,
            "stream": False
        }
    )

    data = response.json()

    return data["response"]


def get_category(text):
    prompt = f"""
    Отнеси задачу к одной категории:
    работа, личное, здоровье, обучение, другое.

    Задача: {text}

    Ответ только одним словом.
    """

    return ask_ollama(prompt).strip().lower()


def estimate_time(text):
    prompt = f"""
    Оцени сколько минут займет задача:
    {text}

    Ответ только числом.
    """

    result = ask_ollama(prompt)

    # защита от мусора
    digits = "".join([c for c in result if c.isdigit()])

    return int(digits) if digits else 10