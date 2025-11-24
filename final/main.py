# final/main.py
from __future__ import annotations
import cmd

from . import pkms, task_manager
from .pkms import find_note_by_id
from .ai_agents import summarize_note_for_artist, suggest_practice_routine
from .storage import log_command



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

  # Notes (PKMS): Your Brain, Dump theory, observations, class notes, anatomy breakdown, etc.
  add-note                    - create a new note
  list-notes                  - list all notes
  view-note <id>              - show one note
  search-notes <query>        - search title/content/tags
  filter-notes tag <name>     - list notes that contain a specific tag
  delete-note <id>            - delete a note (with confirmation)
  edit-note <id>              - edit a note



  # Tasks: Your drawing assignments, practice routines, challenges, etc.
  add-task                    - create a new task
  list-tasks [status]         - list tasks (optionally filter by todo/in-progress/done)
  complete-task <id>          - mark a task as done
  start-task <id>             - mark a task as in-progress
  delete-task <id>            - delete a task
  search-tasks <query>        - search tasks by title/description  
  edit-task <id>              - edit a task

  # AI helpers: Make things easier with AI
  ai-summarize-note <id>      - summarize a note as a short tip
  ai-generate-practice <id>   - generate practice drills from a task
  ai-skill-analysis <id>      - analyze a note and get strengths, weaknesses, plan
  ai-mentor <question>        - ask the AI art mentor a question
  ai-critique <description>   - get AI critique on your artwork description (make sure it's detailed! for best results, it's independent of your notes/tasks)
  ai-anatomy <species> <body_part>   - get deep anatomical explanation for any species and body part (bones, muscles, function)

          
  help                        - show this help
  quit / exit                 - exit the program
""")


def handle_command(line: str) -> bool:
    log_command(line)

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
            pkms.edit_note(nid)
        except ValueError:
            print("Invalid note ID.")
        return True

    if cmd == "search-notes":
        if not args:
            print("Usage: search-notes <query>")
            return True
        query = " ".join(args)
        pkms.search_notes(query)
        return True
    
    # ----- Delete Note -----
    if cmd == "delete-note":
        if not args:
            print("Usage: delete-note <id>")
            return True
        try:
            note_id = int(args[0])
        except ValueError:
            print("Note id must be an integer.")
            return True
        pkms.delete_note_interactive(note_id)
        return True

    
    # ----- Filter Notes by Tag -----
    if cmd == "filter-notes":
        if len(args) < 2 or args[0] != "tag":
            print("Usage: filter-notes tag <tagname>")
            return True

        tag = " ".join(args[1:])
        pkms.filter_notes_by_tag(tag)
        return True


    # ----- Tasks -----
    if cmd == "add-task":
        task_manager.add_task_interactive()
        return True
    
    if cmd == "start-task":
        if not args:
            print("Usage: start-task <id>")
            return True

        try:
            task_id = int(args[0])
        except ValueError:
            print("Task id must be an integer.")
            return True
        task_manager.start_task(task_id)
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
            task_manager.edit_task(tid)
        except ValueError:
            print("Invalid task ID.")
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
    
    if cmd == "ai-generate-practice":
        if not args:
            print("Usage: ai-generate-practice <task_id>")
            return True

        try:
            task_id = int(args[0])
        except ValueError:
            print("Task id must be an integer.")
            return True

        from .task_manager import find_task_by_id
        task = find_task_by_id(task_id)

        if not task:
            print(f"No task #{task_id} found.")
            return True

        from .ai_agents import generate_practices_from_task

        try:
            practices = generate_practices_from_task(task)
            print("\nPractice Drills:")
            print("-----------------------------------")
            print(practices)
            print("-----------------------------------")
        except Exception as e:
            print(f"Error calling AI: {e}")

        return True
    
    if cmd == "ai-skill-analysis":
        if not args:
            print("Usage: ai-skill-analysis <note_id>")
            return True

        try:
            nid = int(args[0])
        except:
            print("Note ID must be an integer.")
            return True

        note = find_note_by_id(nid)
        if not note:
            print(f"No note #{nid} found.")
            return True

        from .ai_agents import analyze_skill_from_note
        
        try:
            report = analyze_skill_from_note(note)
            print("\nSkill Analysis Report:\n------------------------")
            print(report)
            print("------------------------")
        except Exception as e:
            print(f"Error calling AI: {e}")
        return True
    
        # ----- AI MENTOR -----
    if cmd == "ai-mentor":
        if not args:
            print("Enter a question after 'ai-mentor', e.g., ai-mentor how do I improve gesture?")
            return True

        question = " ".join(args)

        from .ai_agents import mentor_chat

        try:
            answer = mentor_chat(question)
            print("\nMentor Response:\n-------------------")
            print(answer)
            print("\n-------------------")
        except Exception as e:
            print(f"Error calling AI: {e}")

        return True

    if cmd == "ai-critique":
        if not args:
            print("Usage: ai-critique <your description>")
            return True

        description = " ".join(args)

        from .ai_agents import critique_artwork

        try:
            critique = critique_artwork(description)
            print("\nArt Critique:\n-------------------")
            print(critique)
            print("-------------------")
        except Exception as e:
            print(f"Error calling AI: {e}")

        return 
    
    if cmd == "ai-anatomy":
        if len(args) < 2:
            print("Usage: ai-anatomy <species> <body_part>")
            return True

        species = args[0]
        body_part = " ".join(args[1:])

        from .ai_agents import anatomy_explain

        try:
            result = anatomy_explain(species, body_part)
            print("\nAnatomy Analysis:\n-------------------")
            print(result)
            print("-------------------")
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
