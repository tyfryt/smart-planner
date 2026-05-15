# Smart Planner AI

Smart Planner AI — это простой планировщик задач на Python с использованием SQLite и локального ИИ через Ollama.

## Возможности

- Добавление задач  
- Просмотр задач  
- Удаление задач  
- Автоматическая категория задачи через ИИ  
- Оценка времени выполнения через ИИ  
- Хранение данных в SQLite  

## Технологии

- Python  
- SQLite  
- Ollama  
- Mistral  
- GitHub
- FastAPI

## Структура проекта

smart_planner/

- main.py — главное меню  
- database.py — работа с базой данных  
- ai_service.py — работа с ИИ  
- task_service.py — логика задач  
- tasks.db — база данных  
- requirements.txt — зависимости  
- README.md  

## Установка и запуск

Установка зависимостей:

pip install -r requirements.txt
pip install fastapi uvicorn

Запуск Ollama:

ollama run mistral

Запуск проекта:

в терминале
uvicorn main:app --reload

## Пример работы

Задача:
убраться дома

Категория (ИИ):
личное

Время (ИИ):
40 минут

## Видео с работой

[https://drive.google.com/drive/u/1/home](https://drive.google.com/file/d/1TMb5FMgeOZS8Yw4qEiKlRRqa-R9RQBHl/view?usp=sharing)


## ИИ использовался для:
- генерации кода  
- помощи с ошибками  
- интеграции SQLite  
