from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import os

# Прямые импорты без точек
import database
import task_service

app = FastAPI(title="Smart Planner")

# Инициализация базы данных
database.create_table()

# API Эндпоинты
@app.post("/api/tasks")
def add_task(title: str):
    task = task_service.add_task(title)
    return {"status": "ok", "task": task}

@app.get("/api/tasks")
def get_tasks():
    return task_service.get_tasks()

@app.delete("/api/tasks/{task_id}")
def delete_task(task_id: int):
    success = task_service.delete_task(task_id)
    if not success:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"status": "deleted"}

# Главная страница (Фронтенд)
@app.get("/")
def read_index():
    # Ищет index.html в той же папке, где лежит main.py
    return FileResponse(os.path.join(os.path.dirname(__file__), "index.html"))