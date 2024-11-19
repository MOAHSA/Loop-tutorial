import random

# Task tracker application
tasks = []

# Counter-Controlled Loop: Add some sample tasks automatically
print("Initializing sample tasks...")
for i in range(1, 6):  # Counter-controlled loop
    tasks.append(f"Sample Task {i}")
print("Sample tasks added.\n")

# Infinite Loop: Main menu
while True:
    print("\nTask Tracker Menu:")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Mark Task as Done")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    # Condition-Controlled Loop: Validate user input
    while choice not in ['1', '2', '3', '4', '5']:
        choice = input("Invalid choice. Please enter a number between 1 and 5: ")

    if choice == '1':  # View tasks
        print("\nYour Tasks:")
        # Sentinel-Controlled Loop: Stop when tasks are exhausted
        for task in tasks:
            print(f"- {task}")
        if not tasks:
            print("No tasks available.")

    elif choice == '2':  # Add a new task
        new_task = input("Enter the new task: ")
        tasks.append(new_task)
        print(f"Task '{new_task}' added successfully!")

    elif choice == '3':  # Mark a task as done
        if not tasks:
            print("No tasks to mark as done.")
            continue

        print("\nTasks:")
        for i, task in enumerate(tasks):
            print(f"{i + 1}. {task}")
        # Event-Controlled Loop: Break when valid input is received
        while True:
            try:
                task_number = int(input("Enter the number of the task to mark as done: "))
                if 1 <= task_number <= len(tasks):
                    tasks[task_number - 1] += " (Done)"
                    print(f"Task {task_number} marked as done!")
                    break
                else:
                    print("Invalid task number. Try again.")
            except ValueError:
                print("Please enter a valid number.")

    elif choice == '4':  # Delete a task
        if not tasks:
            print("No tasks to delete.")
            continue

        print("\nTasks:")
        for i, task in enumerate(tasks):
            print(f"{i + 1}. {task}")
        # Event-Controlled Loop: Break when valid input is received
        while True:
            try:
                task_number = int(input("Enter the number of the task to delete: "))
                if 1 <= task_number <= len(tasks):
                    deleted_task = tasks.pop(task_number - 1)
                    print(f"Task '{deleted_task}' deleted successfully!")
                    break
                else:
                    print("Invalid task number. Try again.")
            except ValueError:
                print("Please enter a valid number.")

    elif choice == '5':  # Exit
        print("Exiting Task Tracker. Goodbye!")
        break

    else:
        print("Unexpected choice. Please try again.")

