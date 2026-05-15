from database import connect
from ai_service import get_category, estimate_time


def add_task(title):
    category = get_category(title)
    estimated_time = estimate_time(title)

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

    cursor.execute("SELECT * FROM tasks")
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