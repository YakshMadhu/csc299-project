# final/task_manager.py
from __future__ import annotations
from typing import Optional

from .models import Task
from .storage import load_tasks, save_tasks, next_task_id


def add_task_interactive() -> Task:
    tasks = load_tasks()
    tid = next_task_id(tasks)

    print(">>> Creating a new task")
    title = input("Title: ").strip()
    description = input("Description: ").strip()
    priority = input("Priority [low/medium/high] (default: medium): ").strip() or "medium"
    category = input("Category (e.g., gesture, project, study) [optional]: ").strip() or None
    due_date = input("Due date (YYYY-MM-DD) [optional]: ").strip() or None

    task = Task.create(
        task_id=tid,
        title=title,
        description=description,
        priority=priority,
        category=category,
        due_date=due_date,
    )
    tasks.append(task)
    save_tasks(tasks)

    print(f"Saved task #{task.id}")
    return task


def list_tasks(status_filter: Optional[str] = None) -> None:
    tasks = load_tasks()
    if status_filter:
        status_filter = status_filter.lower().strip()
        tasks = [t for t in tasks if t.status == status_filter]

    if not tasks:
        print("No tasks. Add one with `add-task`.")
        return

    print("Your tasks:")
    for t in sorted(tasks, key=lambda x: (x.status, x.priority, x.id)):
        cat = t.category or "-"
        due = t.due_date or "-"
        print(f"- [{t.id}] ({t.status}/{t.priority}) [{cat}] due {due}: {t.title}")


def find_task_by_id(task_id: int) -> Optional[Task]:
    tasks = load_tasks()
    for t in tasks:
        if t.id == task_id:
            return t
    return None


def mark_task_done(task_id: int) -> None:
    tasks = load_tasks()
    found = False
    for t in tasks:
        if t.id == task_id:
            t.mark_done()
            found = True
            break
    if not found:
        print(f"No task found with id {task_id}.")
        return
    save_tasks(tasks)
    print(f"Task #{task_id} marked as done.")


def delete_task(task_id: int) -> None:
    tasks = load_tasks()
    new_tasks = [t for t in tasks if t.id != task_id]
    if len(new_tasks) == len(tasks):
        print(f"No task found with id {task_id}.")
        return
    save_tasks(new_tasks)
    print(f"Deleted task #{task_id}.")


def search_tasks(query: str) -> None:
    query = query.lower().strip()
    tasks = load_tasks()
    matches = [
        t for t in tasks
        if query in t.title.lower()
        or query in t.description.lower()
        or (t.category and query in t.category.lower())
    ]
    if not matches:
        print(f"No tasks matched '{query}'.")
        return
    print(f"Tasks matching '{query}':")
    for t in matches:
        cat = t.category or "-"
        print(f"- [{t.id}] ({t.status}) [{cat}] {t.title}")
