





import os


# Function to show tasks
def show_task(tasks):
    if not tasks:
        print("No tasks found.")
    else:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")


# Function to add a task
def add_task(tasks, new_task):
    tasks.append(new_task)
    print("Task added successfully.")


# Function to update a task
def update_task(tasks, index, updated_task):
    if 1 <= index <= len(tasks):
        tasks[index - 1] = updated_task
        print("Task updated successfully.")
    else:
        print("Invalid task index.")


# Function to delete a task
def delete_task(tasks, index):
    if 1 <= index <= len(tasks):
        deleted_task = tasks.pop(index - 1)
        print(f"Task '{deleted_task}' deleted successfully.")
    else:
        print("Invalid task index.")


# Function to save tasks to a file
def save_task_to_file(file_path, tasks):
    with open(file_path, "w") as file:
        for task in tasks:
            file.write(f"{task}\n")


# Function to load tasks from a file
def load_task_from_file(file_path):
    tasks = []
    try:
        if os.path.exists(file_path):
            with open(file_path, "r") as file:
                tasks = file.read().splitlines()
    except FileNotFoundError:
        print(f"File '{file_path}' not found. Creating a new one.")
    return tasks


# Main function
def main():
    file_path = "todo_list.txt"
    tasks = load_task_from_file(file_path)

    while True:
        print("\n====== To-Do List ======")
        print("1. Show Task")
        print("2. Add Task")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Save Task")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")
        if choice == "1":
            show_task(tasks)
        elif choice == "2":
            new_task = input("Enter the task to add: ")
            add_task(tasks, new_task)
        elif choice == "3":
            index = int(input("Enter the task index to update: "))
            updated_task = input("Enter the updated task: ")
            update_task(tasks, index, updated_task)
        elif choice == "4":
            index = int(input("Enter the task index to delete: "))
            delete_task(tasks, index)
        elif choice == "5":
            save_task_to_file(file_path, tasks)
            print("Tasks saved successfully.")
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
