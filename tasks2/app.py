import tkinter as tk
from tkinter import messagebox, simpledialog
import json
import hashlib
from pathlib import Path
from datetime import datetime
import pytz  # <- run "pip install pytz" if not installed

# ---------- File Paths ----------
USERS_FILE = Path(__file__).with_name("users.json")

# ---------- Helpers ----------
def load_users():
    if USERS_FILE.exists():
        with open(USERS_FILE, "r") as f:
            data = json.load(f)
            if isinstance(data, dict):
                return data
    return {}

def save_users(users):
    with open(USERS_FILE, "w") as f:
        json.dump(users, f, indent=2)

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# ---------- Task Utilities ----------
def get_task_file(username):
    return Path(__file__).with_name(f"tasks_{username}.json")

def load_tasks(username):
    task_file = get_task_file(username)
    if task_file.exists():
        with open(task_file, "r") as f:
            return json.load(f)
    return []

def save_tasks(username, tasks):
    task_file = get_task_file(username)
    with open(task_file, "w") as f:
        json.dump(tasks, f, indent=2)

# ---------- Authentication ----------
def signup():
    username = entry_username.get().strip()
    password = entry_password.get().strip()

    if not username or not password:
        messagebox.showwarning("Warning", "Please enter both username and password.")
        return

    users = load_users()
    if username in users:
        messagebox.showerror("Error", "Username already exists!")
        return

    users[username] = hash_password(password)
    save_users(users)
    messagebox.showinfo("Success", "Account created successfully! Please log in.")
    entry_username.delete(0, tk.END)
    entry_password.delete(0, tk.END)

def login():
    username = entry_username.get().strip()
    password = entry_password.get().strip()
    users = load_users()

    if username not in users:
        messagebox.showerror("Error", "No such user found. Please sign up first.")
        return

    if users[username] == hash_password(password):
        messagebox.showinfo("Welcome", f"Hello {username}! You’re now logged in.")
        open_task_window(username)
    else:
        messagebox.showerror("Error", "Incorrect password.")

def forgot_password():
    username = entry_username.get().strip()
    users = load_users()
    if username in users:
        messagebox.showinfo("Reset Link Sent",
                            f"A reset link has been sent to {username}@example.com (simulated).")
    else:
        messagebox.showwarning("Not Found", "No such user found.")

# ---------- Task Manager ----------
def open_task_window(username):
    task_window = tk.Toplevel(root)
    task_window.title(f"{username}'s Task Manager")
    task_window.geometry("500x430")
    task_window.resizable(False, False)

    # --- Load & Refresh ---
    def refresh_tasks(show_hidden=False):
        listbox_tasks.delete(0, tk.END)
        tasks = load_tasks(username)
        for task in tasks:
            if not show_hidden and task.get("hidden", False):
                continue
            status = "[Hidden] " if task.get("hidden", False) else ""
            timestamp = task.get("time", "No time")
            listbox_tasks.insert(tk.END, f"{status}{task['task']}  ({timestamp})")

    # --- Add Task ---
    def add_task():
        task_text = entry_task.get().strip()
        if not task_text:
            messagebox.showwarning("Warning", "Please enter a task.")
            return

        # Get Chicago time
        chicago_tz = pytz.timezone("America/Chicago")
        current_time = datetime.now(chicago_tz)
        timestamp = current_time.strftime("%Y-%m-%d %I:%M %p")

        tasks = load_tasks(username)
        # Add newest first
        new_task = {"task": task_text, "time": timestamp, "hidden": False}
        tasks.insert(0, new_task)

        save_tasks(username, tasks)
        entry_task.delete(0, tk.END)
        refresh_tasks(show_hidden_var.get())

    # --- Hide Task ---
    def hide_task():
        selection = listbox_tasks.curselection()
        if not selection:
            messagebox.showwarning("Warning", "Select a task to hide.")
            return

        index = selection[0]
        all_tasks = load_tasks(username)

        # Build a list of currently displayed (non-hidden) tasks
        visible_tasks = [t for t in all_tasks if not t.get("hidden", False) or show_hidden_var.get()]

        if not visible_tasks or index >= len(visible_tasks):
            return

        task_to_hide = visible_tasks[index]["task"]

        for t in all_tasks:
            if t["task"] == task_to_hide:
                t["hidden"] = True

        save_tasks(username, all_tasks)

        # Force full refresh
        refreshed = load_tasks(username)
        listbox_tasks.delete(0, tk.END)
        for t in refreshed:
            if not t.get("hidden", False) or show_hidden_var.get():
                ts = t.get("time", "No time")
                listbox_tasks.insert(tk.END, f"{t['task']}  ({ts})")

    # --- Unhide All ---
    def unhide_all():
        tasks = load_tasks(username)
        for t in tasks:
            t["hidden"] = False
        save_tasks(username, tasks)
        refresh_tasks(show_hidden_var.get())

    # --- Delete Task ---
    def delete_task():
        selection = listbox_tasks.curselection()
        if not selection:
            messagebox.showwarning("Warning", "Select a task to delete.")
            return
        index = selection[0]
        tasks = load_tasks(username)
        visible_tasks = [t for t in tasks if not t.get("hidden", False) or show_hidden_var.get()]
        if index < len(visible_tasks):
            task_to_delete = visible_tasks[index]["task"]
            confirm = messagebox.askyesno("Confirm Delete", f"Are you sure you want to delete '{task_to_delete}'?")
            if confirm:
                tasks = [t for t in tasks if t["task"] != task_to_delete]
                save_tasks(username, tasks)
                refresh_tasks(show_hidden_var.get())

    # --- Search Task ---
    def search_task():
        keyword = simpledialog.askstring("Search Task", "Enter keyword:")
        if not keyword:
            return
        tasks = load_tasks(username)
        matches = [t for t in tasks if keyword.lower() in t["task"].lower() and not t.get("hidden", False)]
        listbox_tasks.delete(0, tk.END)
        if matches:
            for m in matches:
                ts = m.get("time", "No time")
                listbox_tasks.insert(tk.END, f"{m['task']}  ({ts})")
        else:
            messagebox.showinfo("Search", "No matching tasks found.")

    # ---------- UI ----------
    tk.Label(task_window, text=f"Welcome, {username}!", font=("Arial", 12, "bold")).pack(pady=10)

    # Entry + Add
    frame_entry = tk.Frame(task_window)
    frame_entry.pack(pady=5)

    entry_task = tk.Entry(frame_entry, width=35)
    entry_task.pack(side=tk.LEFT, padx=5)
    tk.Button(frame_entry, text="Add Task", command=add_task).pack(side=tk.LEFT)

    # Listbox
    listbox_tasks = tk.Listbox(task_window, width=65, height=10)
    listbox_tasks.pack(pady=10)

    # Buttons
    frame_buttons = tk.Frame(task_window)
    frame_buttons.pack()

    tk.Button(frame_buttons, text="Search", command=search_task).pack(side=tk.LEFT, padx=5)
    tk.Button(frame_buttons, text="Hide Selected", command=hide_task).pack(side=tk.LEFT, padx=5)
    tk.Button(frame_buttons, text="Unhide All/Go back", command=unhide_all).pack(side=tk.LEFT, padx=5)
    tk.Button(frame_buttons, text="Delete Selected", command=delete_task).pack(side=tk.LEFT, padx=5)

    # Checkbox for hidden toggle
    show_hidden_var = tk.BooleanVar()
    show_hidden_check = tk.Checkbutton(task_window, text="Show Hidden", variable=show_hidden_var,
                                       command=lambda: refresh_tasks(show_hidden_var.get()))
    show_hidden_check.pack(pady=5)

    refresh_tasks()

# ---------- Login Window ----------
root = tk.Tk()
root.title("Task Manager Login")
root.geometry("320x260")
root.resizable(False, False)

tk.Label(root, text="Username").pack(pady=5)
entry_username = tk.Entry(root, width=30)
entry_username.pack()

tk.Label(root, text="Password").pack(pady=5)
entry_password = tk.Entry(root, width=30, show="*")
entry_password.pack()

tk.Button(root, text="Login", width=20, command=login).pack(pady=5)
tk.Button(root, text="Sign Up", width=20, command=signup).pack(pady=5)
tk.Button(root, text="Forgot Password", width=20, command=forgot_password).pack(pady=5)

root.mainloop()
