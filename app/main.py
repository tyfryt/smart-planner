from fastapi import FastAPI, HTTPException
import database
import task_service

app = FastAPI(title="Smart Planner")

database.create_table()


@app.post("/tasks")
def add_task(title: str):
    task = task_service.add_task(title)
    return {"status": "ok", "task": task}


@app.get("/tasks")
def get_tasks():
    return task_service.get_tasks()


@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    success = task_service.delete_task(task_id)

    if not success:
        raise HTTPException(status_code=404, detail="Task not found")

    return {"status": "deleted"}