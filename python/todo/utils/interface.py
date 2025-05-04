import json
from pydantic import ValidationError

from python.todo.models.Task import Task
from python.todo.utils.validateData import TaskModel, UpdateTaskModel

task = Task()

def display_menu():
    print("\nTask Manager")
    print("1. Get Tasks")
    print("2. Get Task by ID")
    print("3. Add Task")
    print("4. Mark Task as Complete")
    print("5. Update Task")
    print("6. Delete Task")
    print("7. Exit")

def get_tasks():
    tasks = task.getTasks()
    print("Tasks:", tasks)

def get_task_by_id():
    task_id = input("Enter task ID: ")
    if task_id:
        try:
            task_data = task.getTaskById(task_id)
            print("Task:", task_data)
        except Exception as e:
            print("Error:", str(e))

def add_task():
    title = input("Enter task title: ")
    folder = input("Enter folder (optional, default: All): ") or "All"
    description = input("Enter description: ")
    
    data = {
        "title": title.strip(),
        "folder": folder.strip(),
        "description": description.strip(),
    }
    
    try:
        valid_task = TaskModel(**data)
        task.addTask(valid_task.dict())
        print("Task added successfully!")
    except ValidationError as e:
        print("Validation Error:", e.json())

def mark_as_complete():
    task_id = input("Enter task ID: ")
    if task_id:
        result = task.markTaskIsComplete(task_id)

def update_task():
    task_id = input("Enter task ID: ")
    title = input("Enter new title (optional): ").strip()
    folder = input("Enter new folder (optional, default: All): ").strip() or "All"
    description = input("Enter new description (optional): ").strip()

    data = {k: v for k, v in {"title": title, "folder": folder, "description": description}.items() if v}

    try:
        valid_task = UpdateTaskModel(**data)
        task.updateTaskById(valid_task.dict(), task_id)
    except ValidationError as e:
        print("Validation Error:", e.json())

def delete_task():
    task_id = input("Enter task ID: ")
    if task_id:
        task.deleteTaskById(task_id)

def user_interface():
    while True:
        display_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            get_tasks()
        elif choice == "2":
            get_task_by_id()
        elif choice == "3":
            add_task()
        elif choice == "4":
            mark_as_complete()
        elif choice == "5":
            update_task()
        elif choice == "6":
            delete_task()
        elif choice == "7":
            print("Exiting...")
            break
        else:
            print("Invalid choice, please try again.")

