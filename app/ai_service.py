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


def get_category(task):
    prompt = f"""
    Отнеси задачу к одной категории:
    работа, личное, здоровье, обучение, другое.

    Задача: {task}

    Верни только категорию.
    """

    return ask_ollama(prompt).strip().lower()


def estimate_time(task):
    prompt = f"""
    Оцени сколько минут займёт задача:
    {task}

    Верни только число.
    """

    result = ask_ollama(prompt)

    try:
        return int(result.strip())
    except:
        return 30