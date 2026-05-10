import database
import task_service


database.create_table()


def menu():
    while True:
        print("""
=== SMART PLANNER ===

1. Add task
2. Show tasks
3. Delete task
4. Exit
""")

        choice = input("Choose: ")

        if choice == "1":
            title = input("Task: ")
            task_service.add_task(title)

        elif choice == "2":
            task_service.show_tasks()

        elif choice == "3":
            try:
                task_id = int(input("Task ID: "))
                task_service.delete_task(task_id)
            except:
                print("Only numbers!")

        elif choice == "4":
            print("Bye!")
            break

        else:
            print("Invalid choice")


menu()