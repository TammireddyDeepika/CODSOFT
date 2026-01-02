import tkinter as tk
from tkinter import messagebox
import os

FILENAME = "todo_data.txt"


# Load tasks from file
def load_tasks():
    tasks = []
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as file:
            tasks = [line.strip() for line in file.readlines()]
    return tasks


# Save tasks to file
def save_tasks(task_list):
    with open(FILENAME, "w") as file:
        for task in task_list:
            file.write(task + "\n")


# Main GUI Class
class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.root.geometry("400x500")
        self.root.configure(bg="#E8F6F3")

        # Title
        tk.Label(root, text="TO-DO LIST", font=("Arial", 20, "bold"),
                 bg="#E8F6F3", fg="#117864").pack(pady=10)

        # Task Entry
        self.task_entry = tk.Entry(root, font=("Arial", 14), width=25, bd=2)
        self.task_entry.pack(pady=10)

        # Buttons Frame
        btn_frame = tk.Frame(root, bg="#E8F6F3")
        btn_frame.pack()

        tk.Button(btn_frame, text="Add Task", width=12, font=("Arial", 12),
                  command=self.add_task, bg="#1ABC9C", fg="white").grid(row=0, column=0, padx=5)

        tk.Button(btn_frame, text="Delete Task", width=12, font=("Arial", 12),
                  command=self.delete_task, bg="#CB4335", fg="white").grid(row=0, column=1, padx=5)

        tk.Button(btn_frame, text="Mark Done", width=12, font=("Arial", 12),
                  command=self.mark_done, bg="#5DADE2", fg="white").grid(row=0, column=2, padx=5)

        # Task Listbox
        self.listbox = tk.Listbox(root, height=15, width=45,
                                  font=("Arial", 12), bd=2, selectbackground="#A2D9CE")
        self.listbox.pack(pady=15)

        # Load existing tasks
        self.tasks = load_tasks()
        for t in self.tasks:
            self.listbox.insert(tk.END, t)

    # Add task
    def add_task(self):
        task = self.task_entry.get().strip()
        if task:
            self.listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
            self.save_all()
        else:
            messagebox.showwarning("Warning", "Please enter a task.")

    # Delete selected task
    def delete_task(self):
        try:
            selected_index = self.listbox.curselection()[0]
            self.listbox.delete(selected_index)
            self.save_all()
        except:
            messagebox.showerror("Error", "Please select a task to delete.")

    # Mark task as done
    def mark_done(self):
        try:
            idx = self.listbox.curselection()[0]
            task = self.listbox.get(idx) + " ✔"
            self.listbox.delete(idx)
            self.listbox.insert(idx, task)
            self.save_all()
        except:
            messagebox.showerror("Error", "Please select a task to mark.")

    # Save all tasks
    def save_all(self):
        all_tasks = self.listbox.get(0, tk.END)
        save_tasks(all_tasks)


# Run App
root = tk.Tk()
app = ToDoApp(root)
root.mainloop()
