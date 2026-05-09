import sqlite3

DB_NAME = "tasks.db"


def connect():
    return sqlite3.connect(DB_NAME)


def init_db():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        category TEXT,
        est_time INTEGER
    )
    """)

    conn.commit()
    conn.close()


def add_task(title, category, est_time):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO tasks (title, category, est_time)
        VALUES (?, ?, ?)
    """, (title, category, est_time))

    conn.commit()
    conn.close()


def get_tasks():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM tasks")
    data = cursor.fetchall()

    conn.close()
    return data


def delete_task(task_id):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))

    conn.commit()
    conn.close()