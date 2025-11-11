import json
import sys

DATA_FILE = "tasks.json"

def load_tasks():
    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open(DATA_FILE, "w") as f:
        json.dump(tasks, f, indent=2)

def add_task(task):
    tasks = load_tasks()
    tasks.append({"task": task})
    save_tasks(tasks)
    print(f"✅ Added task: {task}")

def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
    else:
        print("📋 Your Tasks:")
        for i, t in enumerate(tasks, 1):
            print(f"{i}. {t['task']}")

def search_tasks(keyword):
    tasks = load_tasks()
    matches = [t['task'] for t in tasks if keyword.lower() in t['task'].lower()]
    if matches:
        print("🔍 Matching tasks:")
        for m in matches:
            print("-", m)
    else:
        print("No matching tasks found.")

def main():
    if len(sys.argv) < 2:
        print("Usage: python tasks.py [add|list|search] [task/keyword]")
        return

    command = sys.argv[1]

    if command == "add" and len(sys.argv) > 2:
        add_task(" ".join(sys.argv[2:]))
    elif command == "list":
        list_tasks()
    elif command == "search" and len(sys.argv) > 2:
        search_tasks(" ".join(sys.argv[2:]))
    else:
        print("Invalid command or missing argument.")

if __name__ == "__main__":
    main()
