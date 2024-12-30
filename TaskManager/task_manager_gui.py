
import sqlite3
from tkinter import *
from tkinter import messagebox, ttk


# Initialize the SQLite database
def initialize_db():
    conn = sqlite3.connect("tasks.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            status TEXT CHECK(status IN ('To Do', 'In Progress', 'Done')) DEFAULT 'To Do',
            priority INTEGER CHECK(priority BETWEEN 1 AND 5) DEFAULT 3
        )
    """)
    conn.commit()
    conn.close()


# Add a new task
def add_task():
    title = title_entry.get()
    description = description_entry.get("1.0", END).strip()
    priority = priority_var.get()

    if not title:
        messagebox.showerror("Error", "Task title cannot be empty!")
        return

    conn = sqlite3.connect("tasks.db")
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO tasks (title, description, priority)
        VALUES (?, ?, ?)
    """, (title, description, priority))
    conn.commit()
    conn.close()

    messagebox.showinfo("Success", "Task added successfully!")
    title_entry.delete(0, END)
    description_entry.delete("1.0", END)
    load_tasks()


# Load tasks into the Treeview
def load_tasks(status_filter=None):
    for item in task_tree.get_children():
        task_tree.delete(item)

    conn = sqlite3.connect("tasks.db")
    cursor = conn.cursor()
    query = "SELECT * FROM tasks"
    params = ()
    if status_filter:
        query += " WHERE status = ?"
        params = (status_filter,)
    query += " ORDER BY priority ASC"
    cursor.execute(query, params)
    tasks = cursor.fetchall()
    conn.close()

    for task in tasks:
        task_tree.insert("", "end", values=task)


# Update task status
def update_status():
    selected_item = task_tree.selection()
    if not selected_item:
        messagebox.showerror("Error", "Please select a task to update!")
        return

    task_id = task_tree.item(selected_item)["values"][0]
    new_status = status_var.get()

    conn = sqlite3.connect("tasks.db")
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE tasks
        SET status = ?
        WHERE id = ?
    """, (new_status, task_id))
    conn.commit()
    conn.close()

    messagebox.showinfo("Success", "Task status updated successfully!")
    load_tasks()


# Delete selected task
def delete_task():
    selected_item = task_tree.selection()
    if not selected_item:
        messagebox.showerror("Error", "Please select a task to delete!")
        return

    task_id = task_tree.item(selected_item)["values"][0]

    conn = sqlite3.connect("tasks.db")
    cursor = conn.cursor()
    cursor.execute("""
        DELETE FROM tasks
        WHERE id = ?
    """, (task_id,))
    conn.commit()
    conn.close()

    messagebox.showinfo("Success", "Task deleted successfully!")
    load_tasks()


# Main application window
def main():
    global title_entry, description_entry, priority_var, status_var, task_tree

    initialize_db()

    root = Tk()
    root.title("Task Management System")
    root.geometry("800x600")

    # Title and description input
    Label(root, text="Title:").grid(row=0, column=0, padx=10, pady=10, sticky=W)
    title_entry = Entry(root, width=50)
    title_entry.grid(row=0, column=1, padx=10, pady=10)

    Label(root, text="Description:").grid(row=1, column=0, padx=10, pady=10, sticky=NW)
    description_entry = Text(root, width=50, height=5)
    description_entry.grid(row=1, column=1, padx=10, pady=10)

    # Priority dropdown
    Label(root, text="Priority:").grid(row=2, column=0, padx=10, pady=10, sticky=W)
    priority_var = IntVar(value=3)
    ttk.Combobox(root, textvariable=priority_var, values=[1, 2, 3, 4, 5], width=10).grid(row=2, column=1, padx=10, pady=10, sticky=W)

    # Add Task button
    Button(root, text="Add Task", command=add_task).grid(row=3, column=1, padx=10, pady=10, sticky=E)

    # Task Treeview
    task_tree = ttk.Treeview(root, columns=("ID", "Title", "Description", "Status", "Priority"), show="headings")
    task_tree.heading("ID", text="ID")
    task_tree.heading("Title", text="Title")
    task_tree.heading("Description", text="Description")
    task_tree.heading("Status", text="Status")
    task_tree.heading("Priority", text="Priority")
    task_tree.grid(row=4, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")

    # Scrollbar for the Treeview
    scrollbar = Scrollbar(root, orient=VERTICAL, command=task_tree.yview)
    task_tree.configure(yscroll=scrollbar.set)
    scrollbar.grid(row=4, column=3, sticky="ns")

    # Status update
    Label(root, text="Update Status:").grid(row=5, column=0, padx=10, pady=10, sticky=W)
    status_var = StringVar(value="To Do")
    ttk.Combobox(root, textvariable=status_var, values=["To Do", "In Progress", "Done"], width=15).grid(row=5, column=1, padx=10, pady=10, sticky=W)

    # Buttons for actions
    Button(root, text="Update Status", command=update_status).grid(row=6, column=0, padx=10, pady=10, sticky=W)
    Button(root, text="Delete Task", command=delete_task).grid(row=6, column=1, padx=10, pady=10, sticky=W)

    # Filter buttons
    Button(root, text="Show All", command=lambda: load_tasks()).grid(row=7, column=0, padx=10, pady=10)
    Button(root, text="To Do", command=lambda: load_tasks("To Do")).grid(row=7, column=1, padx=10, pady=10)
    Button(root, text="In Progress", command=lambda: load_tasks("In Progress")).grid(row=7, column=2, padx=10, pady=10)
    Button(root, text="Done", command=lambda: load_tasks("Done")).grid(row=7, column=3, padx=10, pady=10)

    load_tasks()
    root.mainloop()


if __name__ == "__main__":
    main()
