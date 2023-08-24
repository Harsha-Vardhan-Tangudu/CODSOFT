import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
from datetime import datetime

class Task:
    def __init__(self, description, due_date):
        self.description = description
        self.due_date = due_date
        self.completed = False

class UniqueToDoListApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Uniquely Yours To-Do List")
        self.geometry("500x600")
        self.configure(bg="#121212")
        self.tasks = []
        self.create_widgets()

    def create_widgets(self):
        self.task_list = tk.Listbox(self, selectmode=tk.SINGLE, bg="#212121", fg="#E1E1E1", font=("Arial", 12))
        self.task_list.pack(padx=20, pady=20, fill=tk.BOTH, expand=True)
        self.refresh_tasks()

        add_button = tk.Button(self, text="✨ Add Task", command=self.add_task, bg="#4CAF50", fg="white", font=("Helvetica", 12, "bold"))
        add_button.pack(pady=10)

        update_button = tk.Button(self, text="🔄 Update Status", command=self.update_task_status, bg="#FFD700", fg="#333", font=("Helvetica", 12, "bold"))
        update_button.pack(pady=10)

        delete_button = tk.Button(self, text="❌ Delete Task", command=self.delete_task, bg="#FF6B6B", fg="white", font=("Helvetica", 12, "bold"))
        delete_button.pack(pady=10)

    def refresh_tasks(self):
        self.task_list.delete(0, tk.END)
        for task in self.tasks:
            status = "✔️ Done" if task.completed else "❌ Not Done"
            self.task_list.insert(tk.END, f"📌 {task.description} - 🗓️ {task.due_date} - {status}")

    def add_task(self):
        description = simpledialog.askstring("Add Task", "Enter task description:")
        if description:
            due_date_str = simpledialog.askstring("Add Task", "Enter due date (YYYY-MM-DD):")
            try:
                due_date = datetime.strptime(due_date_str, "%Y-%m-%d").date()
                task = Task(description, due_date)
                self.tasks.append(task)
                self.refresh_tasks()
            except ValueError:
                messagebox.showerror("Error", "Invalid date format. Please use YYYY-MM-DD.")

    def update_task_status(self):
        selected_index = self.task_list.curselection()
        if selected_index:
            selected_index = selected_index[0]
            task = self.tasks[selected_index]
            new_status = not task.completed
            task.completed = new_status
            self.refresh_tasks()

    def delete_task(self):
        selected_index = self.task_list.curselection()
        if selected_index:
            selected_index = selected_index[0]
            self.tasks.pop(selected_index)
            self.refresh_tasks()

if __name__ == "__main__":
    app = UniqueToDoListApp()
    app.mainloop()
