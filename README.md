/Users/user/PycharmProjects/дом/.venv/bin/python /Users/user/PycharmProjects/дом/smart_planner/main.py 

=== SMART PLANNER ===

1. Add task
2. Show tasks
3. Delete task
4. Exit

Choose: 2
No tasks

=== SMART PLANNER ===

1. Add task
2. Show tasks
3. Delete task
4. Exit

Choose: 1
Task: гулять
Traceback (most recent call last):
  File "/Users/user/PycharmProjects/дом/smart_planner/main.py", line 43, in <module>
    menu()
    ~~~~^^
  File "/Users/user/PycharmProjects/дом/smart_planner/main.py", line 23, in menu
    task_service.add_task(title)
    ~~~~~~~~~~~~~~~~~~~~~^^^^^^^
  File "/Users/user/PycharmProjects/дом/smart_planner/task_service.py", line 11, in add_task
    cursor.execute("""
    ~~~~~~~~~~~~~~^^^^
    INSERT INTO tasks (title, category, estimated_time)
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    VALUES (?, ?, ?)
    ^^^^^^^^^^^^^^^^
    """, (title, category, estimated_time))
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
sqlite3.OperationalError: table tasks has no column named estimated_time

Process finished with exit code 1