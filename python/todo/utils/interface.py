import tkinter as tk
from tkinter import messagebox, simpledialog
from pydantic import ValidationError

from ..models.Task import Task
from .validateData import TaskModel, UpdateTaskModel

task = Task()

class TaskManagerApp:
    def __init__(self, master):
        self.master = master
        master.title("Task Manager")

        self.label = tk.Label(master, text="Task Manager")
        self.label.pack()

        self.get_tasks_button = tk.Button(master, text="Get Tasks", command=self.get_tasks)
        self.get_tasks_button.pack()

        self.get_task_by_id_button = tk.Button(master, text="Get Task by ID", command=self.get_task_by_id)
        self.get_task_by_id_button.pack()

        self.add_task_button = tk.Button(master, text="Add Task", command=self.add_task)
        self.add_task_button.pack()

        self.mark_complete_button = tk.Button(master, text="Mark as Complete", command=self.mark_as_complete)
        self.mark_complete_button.pack()

        self.update_task_button = tk.Button(master, text="Update Task", command=self.update_task)
        self.update_task_button.pack()

        self.delete_task_button = tk.Button(master, text="Delete Task", command=self.delete_task)
        self.delete_task_button.pack()

    def get_tasks(self):
        tasks = task.getTasks()
        messagebox.showinfo("Tasks", f"Tasks: {tasks}")

    def get_task_by_id(self):
        task_id = simpledialog.askstring("Input", "Enter task ID:")
        if task_id:
            try:
                task_data = task.getTaskById(task_id)
                messagebox.showinfo("Task Data", f"Task: {task_data}")
            except Exception as e:
                messagebox.showerror("Error", str(e))

    def add_task(self):
        title = simpledialog.askstring("Input", "Enter task title:")
        folder = simpledialog.askstring("Input", "Enter folder (optional):") or "All"
        description = simpledialog.askstring("Input", "Enter description:")

        data = {
            "title": title.strip(),
            "folder": folder.strip(),
            "description": description.strip(),
        }

        try:
            valid_task = TaskModel(**data)
            task.addTask(valid_task.dict())
            messagebox.showinfo("Success", "Task added successfully!")
        except ValidationError as e:
            messagebox.showerror("Validation Error", e.json())

    def mark_as_complete(self):
        task_id = simpledialog.askstring("Input", "Enter task ID:")
        if task_id:
            result = task.markTaskIsComplete(task_id)
            messagebox.showinfo("Result", f"Task marked as complete: {result}")

    def update_task(self):
        task_id = simpledialog.askstring("Input", "Enter task ID:")
        title = simpledialog.askstring("Input", "Enter new title (optional):")
        folder = simpledialog.askstring("Input", "Enter new folder (optional):") or "All"
        description = simpledialog.askstring("Input", "Enter new description (optional):")

        data = {
            "title": title.strip() if title else None,
            "folder": folder.strip(),
            "description": description.strip() if description else None,
        }

        try:
            valid_task = UpdateTaskModel(**data)
            task.updateTaskById(valid_task.dict(), task_id)
            messagebox.showinfo("Success", "Task updated successfully!")
        except ValidationError as e:
            messagebox.showerror("Validation Error", e.json())

    def delete_task(self):
        task_id = simpledialog.askstring("Input", "Enter task ID:")
        if task_id:
            task.deleteTaskById(task_id)
            messagebox.showinfo("Success", "Task deleted successfully!")

if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManagerApp(root)
    root.mainloop()
