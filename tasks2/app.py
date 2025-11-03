import tkinter as tk
from tkinter import messagebox
import json
import hashlib
from pathlib import Path

# ---------- File Setup ----------
USERS_FILE = Path(__file__).with_name("users.json")

def load_users():
    if USERS_FILE.exists():
        with open(USERS_FILE, "r") as f:
            return json.load(f)
    return {}

def save_users(users):
    with open(USERS_FILE, "w") as f:
        json.dump(users, f, indent=2)

# ---------- Hash Helper ----------
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# ---------- Signup ----------
def signup():
    username = entry_username.get().strip()
    password = entry_password.get().strip()

    if not username or not password:
        messagebox.showwarning("Warning", "All fields are required!")
        return

    users = load_users()
    if username in users:
        messagebox.showerror("Error", "Username already exists!")
        return

    users[username] = hash_password(password)
    save_users(users)
    messagebox.showinfo("Success", "Account created! Please log in.")
    entry_username.delete(0, tk.END)
    entry_password.delete(0, tk.END)

# ---------- Login ----------
def login():
    username = entry_username.get().strip()
    password = entry_password.get().strip()
    users = load_users()

    if username not in users:
        messagebox.showerror("Error", "User not found!")
        return

    if users[username] == hash_password(password):
        messagebox.showinfo("Welcome", f"Hello, {username}! Login successful.")
    else:
        messagebox.showerror("Error", "Incorrect password.")

# ---------- Forgot Password (Simulated) ----------
def forgot_password():
    username = entry_username.get().strip()
    users = load_users()

    if username in users:
        messagebox.showinfo("Reset Sent", f"A reset link has been sent to {username}@example.com")
    else:
        messagebox.showwarning("Not Found", "No such user found!")

# ---------- UI ----------
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
