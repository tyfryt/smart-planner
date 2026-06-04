from database import connect
from ai_service import analyze_task  # Импортируем быструю функцию


def add_task(title):
    # Делаем один запрос к ИИ вместо двух!
    task_analysis = analyze_task(title)
    category = task_analysis["category"]
    estimated_time = task_analysis["estimated_time"]

    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO tasks (title, category, estimated_time)
    VALUES (?, ?, ?)
    """, (title, category, estimated_time))

    conn.commit()

    task_id = cursor.lastrowid
    conn.close()

    return {
        "id": task_id,
        "title": title,
        "category": category,
        "estimated_time": estimated_time
    }


def get_tasks():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("SELECT * ")  # Исправлено: в вашей БД ровно 4 колонки
    rows = cursor.fetchall()
    conn.close()

    return [
        {
            "id": r[0],
            "title": r[1],
            "category": r[2],
            "estimated_time": r[3]
        }
        for r in rows
    ]


def delete_task(task_id):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    conn.commit()

    deleted = cursor.rowcount > 0
    conn.close()

    return deleted