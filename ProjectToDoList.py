#To DO List

tasks = []

print("Welcome to the To-Do List Manager!")

while True:
    print("\n=== To-Do List Menu ===")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":  # View Tasks
        if not tasks:
            print("\nYour to-do list is empty!")
        else:
            print("\nTo-Do List:")
            for i, task in enumerate(tasks, 1):
                status = "✔" if task["completed"] else "✘"
                print(f"{i}. {task['task']} [{status}]")

    elif choice == "2":  # Add Task
        new_task = input("Enter the new task: ")
        tasks.append({"task": new_task, "completed": False})
        print(f"Task '{new_task}' added successfully!")

    elif choice == "3":  # Mark Task as Completed
        if not tasks:
            print("\nYour to-do list is empty!")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(tasks, 1):
                status = "✔" if task["completed"] else "✘"
                print(f"{i}. {task['task']} [{status}]")
            try:
                task_num = int(input("Enter the task number to mark as completed: "))
                if 1 <= task_num <= len(tasks):
                    tasks[task_num - 1]["completed"] = True
                    print("Task marked as completed!")
                else:
                    print("Invalid task number!")
            except ValueError:
                print("Please enter a valid number.")

    elif choice == "4":  # Delete Task
        if not tasks:
            print("\nYour to-do list is empty!")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(tasks, 1):
                status = "✔" if task["completed"] else "✘"
                print(f"{i}. {task['task']} [{status}]")
            try:
                task_num = int(input("Enter the task number to delete: "))
                if 1 <= task_num <= len(tasks):
                    removed_task = tasks.pop(task_num - 1)
                    print(f"Task '{removed_task['task']}' deleted successfully!")
                else:
                    print("Invalid task number!")
            except ValueError:
                print("Please enter a valid number.")

    elif choice == "5":  # Exit
        print("Goodbye! Your tasks have not been saved (runtime only).")
        break

    else:
        print("Invalid choice! Please try again.")