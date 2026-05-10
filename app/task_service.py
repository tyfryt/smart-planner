from smart_planner.app import ai_service, database


def add_task(title):
    category = ai_service.get_category(title)
    estimated_time = ai_service.estimate_time(title)

    conn = database.connect()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO tasks (title, category, estimated_time)
    VALUES (?, ?, ?)
    """, (title, category, estimated_time))

    conn.commit()
    conn.close()

    print("✅ Task added!")


def show_tasks():
    conn = database.connect()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM tasks")

    tasks = cursor.fetchall()

    conn.close()

    if not tasks:
        print("No tasks")
        return

    for task in tasks:
        print(
            f"""
ID: {task[0]}
Task: {task[1]}
Category: {task[2]}
Estimated time: {task[3]} min
------------------------
"""
        )


def delete_task(task_id):
    conn = database.connect()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM tasks WHERE id = ?",
        (task_id,)
    )

    conn.commit()
    conn.close()

    print("🗑 Task deleted")