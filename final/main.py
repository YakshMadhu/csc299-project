# final/main.py
from __future__ import annotations

from . import pkms, task_manager
from .pkms import find_note_by_id
from .ai_agents import summarize_note_for_artist, suggest_practice_routine


BANNER = r"""
========================================
   ArtGrow – PKMS & Task Coach (CLI)
========================================
Type 'help' to see commands.
Type 'quit' or 'exit' to leave.
"""


def print_help() -> None:
    print("""
Commands:

  # Notes (PKMS)
  add-note                    - create a new note
  list-notes                  - list all notes
  view-note <id>              - show one note
  search-notes <query>        - search title/content/tags

  # Tasks
  add-task                    - create a new task
  list-tasks [status]         - list tasks (optionally filter by todo/in-progress/done)
  complete-task <id>          - mark a task as done
  delete-task <id>            - delete a task
  search-tasks <query>        - search tasks

  # AI helpers
  ai-summarize-note <id>      - summarize a note as a short tip
  ai-suggest-practice         - suggest a practice routine

  help                        - show this help
  quit / exit                 - exit the program
""")


def handle_command(line: str) -> bool:
    parts = line.strip().split()
    if not parts:
        return True

    cmd = parts[0].lower()
    args = parts[1:]

    if cmd in ("quit", "exit"):
        return False

    if cmd == "help":
        print_help()
        return True

    # ----- Notes -----
    if cmd == "add-note":
        pkms.add_note_interactive()
        return True

    if cmd == "list-notes":
        pkms.list_notes()
        return True

    if cmd == "view-note":
        if not args:
            print("Usage: view-note <id>")
            return True
        try:
            note_id = int(args[0])
        except ValueError:
            print("Note id must be an integer.")
            return True
        pkms.view_note(note_id)
        return True
    
    if cmd == "edit-note":
        if not args:
            print("Usage: edit-note <id>")
            return True
        try:
            nid = int(args[0])
        except ValueError:
            print("Note id must be an integer.")
            return True

        pkms.edit_note_interactive(nid)
        return True

    if cmd == "search-notes":
        if not args:
            print("Usage: search-notes <query>")
            return True
        query = " ".join(args)
        pkms.search_notes(query)
        return True

    # ----- Tasks -----
    if cmd == "add-task":
        task_manager.add_task_interactive()
        return True

    if cmd == "list-tasks":
        status = args[0] if args else None
        task_manager.list_tasks(status_filter=status)
        return True

    if cmd == "complete-task":
        if not args:
            print("Usage: complete-task <id>")
            return True
        try:
            task_id = int(args[0])
        except ValueError:
            print("Task id must be an integer.")
            return True
        task_manager.mark_task_done(task_id)
        return True

    if cmd == "delete-task":
        if not args:
            print("Usage: delete-task <id>")
            return True
        try:
            task_id = int(args[0])
        except ValueError:
            print("Task id must be an integer.")
            return True
        task_manager.delete_task(task_id)
        return True
    
    if cmd == "edit-task":
        if not args:
            print("Usage: edit-task <id>")
            return True
        try:
            tid = int(args[0])
        except ValueError:
            print("Task id must be an integer.")
            return True

        task_manager.edit_task_interactive(tid)
        return True


    if cmd == "search-tasks":
        if not args:
            print("Usage: search-tasks <query>")
            return True
        query = " ".join(args)
        task_manager.search_tasks(query)
        return True

    # ----- AI -----
    if cmd == "ai-summarize-note":
        if not args:
            print("Usage: ai-summarize-note <id>")
            return True
        try:
            note_id = int(args[0])
        except ValueError:
            print("Note id must be an integer.")
            return True

        note = find_note_by_id(note_id)
        if not note:
            print(f"No note #{note_id} found.")
            return True

        try:
            tip = summarize_note_for_artist(note)
            print("\nAI Tip:\n--------")
            print(tip)
            print("--------")
        except Exception as e:
            print(f"Error calling AI: {e}")
        return True

    if cmd == "ai-suggest-practice":
        print("Describe your current struggles or goals (finish with empty line):")
        lines = []
        while True:
            line = input()
            if not line.strip():
                break
            lines.append(line)
        user_input = "\n".join(lines) if lines else "(no description)"

        try:
            plan = suggest_practice_routine(user_input)
            print("\nSuggested practice routine:\n---------------------------")
            print(plan)
            print("---------------------------")
        except Exception as e:
            print(f"Error calling AI: {e}")
        return True

    # ----- Unknown -----
    print(f"Unknown command: {cmd}. Type 'help' to see commands.")
    return True


def main() -> None:
    print(BANNER)
    print_help()
    while True:
        try:
            line = input("> ")
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye!")
            break
        if not handle_command(line):
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()
