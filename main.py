# 1. Add Tasks: Users should be able to add new tasks to the to-do list. Each task should have a description and can be assigned a due date or priority.
#
# 2. Task List Display: Create a feature to display the list of tasks, including details like task description, due date, and priority.
#
# 3. Task Completion: Users should have the ability to mark tasks as completed, which will move them to a separate completed tasks list.
#
# 4. Update Tasks: Allow users to update task descriptions, due dates, or priorities.
#
# 5. Remove Tasks: Implement the option to remove tasks from the list.

import tkinter as tk


class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.root.geometry("400x650+400+100")

        self.tasks = []
        self.completed_tasks = []
        self.tasks_label = tk.Label(self.root, text="Tasks")
        self.tasks_label.pack(pady=10)

        self.task_listbox = tk.Listbox(self.root, selectmode=tk.SINGLE)
        self.task_listbox.pack(pady=10)
        self.completed_label = tk.Label(self.root, text="Completed Tasks")
        self.completed_label.pack()
        self.completed_listbox = tk.Listbox(self.root, selectmode=tk.SINGLE)
        self.completed_listbox.pack(pady=10)

        self.task_entry = tk.Entry(self.root)
        self.task_entry.pack(pady=5)

        self.add_button = tk.Button(self.root, text="Add Task", command=self.add_task)
        self.add_button.pack()

        self.update_button = tk.Button(self.root, text="Update Task", command=self.update_task)
        self.update_button.pack()

        self.delete_button = tk.Button(self.root, text="Delete Task", command=self.delete_task)
        self.delete_button.pack()

        self.complete_button = tk.Button(self.root, text="Mark Complete", command=self.mark_complete)
        self.complete_button.pack()

    def add_task(self):
        description = self.task_entry.get()
        if description:
            self.tasks.append({"description": description, "completed": False})
            self.update_task_list()
            self.clear_entries()

    def mark_complete(self):
        selected_task = self.get_selected_task()
        if selected_task:
            selected_task["completed"] = True
            self.completed_tasks.append(selected_task)
            self.tasks.remove(selected_task)
            self.update_task_list()
            self.update_completed_list()

    def update_task(self):
        selected_task = self.get_selected_task()
        if selected_task:
            new_description = self.task_entry.get()
            selected_task["description"] = new_description
            self.update_task_list()
            self.clear_entries()

    def delete_task(self):
        selected_task = self.get_selected_task()
        if selected_task:
            self.tasks.remove(selected_task)
            self.update_task_list()
            self.clear_entries()

    def update_task_list(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task["description"])

    def update_completed_list(self):
        self.completed_listbox.delete(0, tk.END)
        for task in self.completed_tasks:
            self.completed_listbox.insert(tk.END, task["description"])

    def clear_entries(self):
        self.task_entry.delete(0, tk.END)

    def get_selected_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            selected_task_index = int(selected_task_index[0])
            return self.tasks[selected_task_index]
        return None

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()

