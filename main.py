import db
import ai

db.init_db()


def menu():
    while True:
        print("\n=== SMART PLANNER ===")
        print("1. Add task")
        print("2. Show tasks")
        print("3. Delete task")
        print("4. Exit")

        choice = input("Choose: ")

        if choice == "1":
            add_task()

        elif choice == "2":
            show_tasks()

        elif choice == "3":
            delete_task()

        elif choice == "4":
            print("Bye 👋")
            break

        else:
            print("Invalid choice")


def add_task():
    title = input("Task: ")

    category = ai.get_category(title)
    time_est = ai.estimate_time(title)

    db.add_task(title, category, time_est)

    print(f"Saved → {category}, {time_est} min")


def show_tasks():
    tasks = db.get_tasks()

    if not tasks:
        print("No tasks")
        return

    print("\nID | TITLE | CATEGORY | TIME")
    print("-" * 40)

    for t in tasks:
        print(f"{t[0]} | {t[1]} | {t[2]} | {t[3]}")


def delete_task():
    try:
        task_id = int(input("ID to delete: "))
        db.delete_task(task_id)
        print("Deleted!")
    except:
        print("Invalid ID")


menu()