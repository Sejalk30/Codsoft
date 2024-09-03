 #To do list!
import tkinter as tk
from tkinter import messagebox, simpledialog

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")

        
        self.tasks = []


        self.create_widgets()

    def create_widgets(self):
        
        self.task_listbox = tk.Listbox(self.root, width=50, height=15, selectmode=tk.SINGLE)
        self.task_listbox.pack(padx=20, pady=10)

        self.task_entry = tk.Entry(self.root, width=40)
        self.task_entry.pack(padx=20, pady=5)

        self.add_button = tk.Button(self.root, text="Add Task", command=self.add_task)
        self.add_button.pack(padx=10, pady=5, side=tk.LEFT)

        self.update_button = tk.Button(self.root, text="Update Task", command=self.update_task)
        self.update_button.pack(padx=10, pady=5, side=tk.LEFT)

        self.delete_button = tk.Button(self.root, text="Delete Task", command=self.delete_task)
        self.delete_button.pack(padx=10, pady=5, side=tk.LEFT)

        self.mark_done_button = tk.Button(self.root, text="Mark as Done", command=self.mark_task_done)
        self.mark_done_button.pack(padx=10, pady=5, side=tk.LEFT)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append({'task': task, 'done': False})
            self.update_task_listbox()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "You must enter a task.")

    def update_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            new_task = simpledialog.askstring("Update Task", "Enter the new task description:")
            if new_task:
                self.tasks[selected_index]['task'] = new_task
                self.update_task_listbox()
            else:
                messagebox.showwarning("Warning", "You must enter a new task description.")
        except IndexError:
            messagebox.showwarning("Warning", "You must select a task to update.")

    def delete_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            del self.tasks[selected_index]
            self.update_task_listbox()
        except IndexError:
            messagebox.showwarning("Warning", "You must select a task to delete.")

    def mark_task_done(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            self.tasks[selected_index]['done'] = True
            self.update_task_listbox()
        except IndexError:
            messagebox.showwarning("Warning", "You must select a task to mark as done.")

    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            status = "Done" if task['done'] else "Pending"
            self.task_listbox.insert(tk.END, f"{task['task']} [{status}]")

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
