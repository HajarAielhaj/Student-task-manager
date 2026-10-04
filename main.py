print("welcome to student task manager")
print("=== Student Task Manager ===")
print("1. Add a task")
print("2. Show tasks")
print("3. Mark a task as completed")
print("4. Delete a task")
print("5. Exit")

tasks = []

while True:
    print("\n=== Student Task Manager ===")
    print("1. Add a task")
    print("2. Show tasks")
    print("3. Mark task as completed")
    print("4. Delete a task")
    print("5. Exit")

    choice = input("Choose an option: ")

    # Choice 1: Add a task
    if choice == "1":
        task = input("Enter your task: ")

        new_task = {
            "title": task,
            "completed": False
        }

        tasks.append(new_task)

        print("Task added successfully!")

    # Choice 2: Show tasks
    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks yet.")
        else:
            print("\nYour tasks:")

            for i, task in enumerate(tasks, start=1):
                if task["completed"]:
                    status = "✓"
                else:
                    status = "○"

                print(i, status, task["title"])

    # Choice 3: Mark task as completed
    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks yet.")
        else:
            print("\nYour tasks:")

            for i, task in enumerate(tasks, start=1):
                print(i, "-", task["title"])

            task_number = int(input("Enter the task number to complete: "))

            if 1 <= task_number <= len(tasks):
                tasks[task_number - 1]["completed"] = True
                print("Task completed!")
            else:
                print("Invalid task number.")

    # Choice 4: Delete a task
    elif choice == "4":
        if len(tasks) == 0:
            print("No tasks yet.")
        else:
            print("\nYour tasks:")

            for i, task in enumerate(tasks, start=1):
                print(i, "-", task["title"])

            task_number = int(input("Enter the task number to delete: "))

            if 1 <= task_number <= len(tasks):
                deleted_task = tasks.pop(task_number - 1)
                print("Task deleted:", deleted_task["title"])
            else:
                print("Invalid task number.")

    # Choice 5: Exit
    elif choice == "5":
        print("Goodbye!")
        break

    # Invalid choice
    else:
        print("Invalid option. Please choose between 1 and 5.")