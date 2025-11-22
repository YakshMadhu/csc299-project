
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

    # --- Call AI for suggestions ---
    from .ai_agents import analyze_task_ai
    try:
        suggestions = analyze_task_ai(title, description)
        print("\nAI Suggestions:")
        print(f"- Recommended priority: {suggestions.get('priority')}")
        print(f"- Category: {suggestions.get('category')}")
        print(f"- Suggested due date: {suggestions.get('due_date')}")
        print(f"- Tip: {suggestions.get('tip')}\n")
    except Exception as e:
        print(f"(AI unavailable: {e})")
        suggestions = {}

    # Use AI recommendations as defaults
    priority = suggestions.get("priority") or "medium"
    category = suggestions.get("category")
    due_date = suggestions.get("due_date")

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


def start_task(task_id: int) -> None:
    tasks = load_tasks()
    found = False
    for t in tasks:
        if t.id == task_id:
            t.mark_in_progress()
            found = True
            break

    if not found:
        print(f"No task found with id {task_id}.")
        return

    save_tasks(tasks)
    print(f"Task #{task_id} marked as in-progress.")


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

def edit_task(task_id: int) -> None:
    tasks = load_tasks()
    from .models import now_iso
    found = False

    for t in tasks:
        if t.id == task_id:
            found = True
            print("Editing Task...")

            new_title = input(f"Title [{t.title}]: ").strip()
            if new_title:
                t.title = new_title

            new_desc = input(f"Description [{t.description}]: ").strip()
            if new_desc:
                t.description = new_desc

            new_priority = input(f"Priority (low/medium/high) [{t.priority}]: ").strip().lower()
            if new_priority in ("low", "medium", "high"):
                t.priority = new_priority

            new_category = input(f"Category [{t.category}]: ").strip()
            if new_category:
                t.category = new_category

            new_due = input(f"Due date (YYYY-MM-DD) [{t.due_date}]: ").strip()
            if new_due:
                t.due_date = new_due

            t.updated_at = now_iso()

            break

    if not found:
        print(f"No task found with id {task_id}.")
        return

    save_tasks(tasks)
    print(f"Task #{task_id} edited successfully.")

