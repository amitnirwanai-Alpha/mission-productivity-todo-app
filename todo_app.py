tasks = []


def show_menu():
    print("\nMission Productivity Menu")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Remove Task")
    print("5. Exit")


def add_task():
    title = input("Enter task name: ")
    priority = input("Enter priority (High/Medium/Low): ")

    task = {
        "title": title,
        "completed": False,
        "priority": priority
    }

    tasks.append(task)
    print("Task added successfully!")


def view_tasks():
    if not tasks:
        print("No tasks available.")
        return

    print("\nYour Tasks:")
    for index, task in enumerate(tasks, start=1):
        status = "Done" if task["completed"] else "Pending"
        print(f"{index}. {task['title']} [{status}] | Priority: {task['priority']}")


def mark_task_completed():
    view_tasks()
    try:
        task_number = int(input("Enter task number to mark as completed: "))
        tasks[task_number - 1]["completed"] = True
        print("Task marked as completed!")
    except (IndexError, ValueError):
        print("Invalid task number.")


def remove_task():
    view_tasks()
    try:
        task_number = int(input("Enter task number to remove: "))
        removed = tasks.pop(task_number - 1)
        print(f"Task '{removed['title']}' removed.")
    except (IndexError, ValueError):
        print("Invalid task number.")


def main():
    while True:
        show_menu()
        choice = input("Choose an option (1-5): ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            mark_task_completed()
        elif choice == "4":
            remove_task()
        elif choice == "5":
            print("Exiting application.")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
