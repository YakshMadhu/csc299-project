# Tasks1 - Command Line Task Manager (2025-10-20 Milestone)

This prototype command-line application allows users to **store, list, and search tasks** using a simple JSON data file.  
It's the simplest version of what my program will become — the **first functional draft** of my task manager project.

It fulfills the CSC299 milestone requirement:

> "Create a prototype command-line application that allows storing, listing, and searching tasks stored in a JSON data file."

---

## ⚙️ How to Run

1. **Open a terminal inside this directory:**
   ```bash
   cd tasks1

2. **Add a new task**:
   ```bash
   python tasks.py add "task"

3. **List all tasks**:
   ```bash
   python tasks.py list

4. **Search for a task**:
   ```bash
   python tasks.py search "keyword"


# Reflection 

Working on this prototype helped me understand how data can be stored, retrieved, and searched through command-line interaction.
Before this, I mostly thought of applications as GUI-based, but this project taught me that a CLI can be both powerful and flexible when the logic behind it is solid.

**What I learned**:

How to use Python’s sys.argv for reading command-line arguments.

How to perform file I/O safely using JSON.

The importance of maintaining a consistent project structure (code, data, docs).

# What still needs improvement

While this prototype works, it’s still very basic.
It only supports adding, listing, and searching — but doesn’t yet allow editing, deleting, or marking tasks as done.
Also, the JSON structure could be extended to include metadata like due dates, priority levels, or completion status.

# Plans for the next prototype

For the next iteration, I intend to:

  1. Add a feature to mark tasks as completed or remove them.

  2. Add unique IDs to tasks to avoid duplicates.

  3. Create a menu-driven interface for easier interaction.

  4. Possibly store tasks using a local database (SQLite) instead of JSON.

  5. Add error handling and input validation for better reliability.

Through these improvements, I hope to evolve this simple command-line project into a more structured, modular, and scalable application.

