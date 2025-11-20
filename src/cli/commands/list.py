"""List command handler."""
import sys
import json
from src.storage import load_tasks, sort_tasks


def list_tasks() -> int:
    """List all drawing tasks in alphabetical order.
    
    Returns:
        Exit code (0 for success, 1 for error)
    """
    try:
        # Load tasks
        tasks = load_tasks()
        
        if not tasks:
            print("No tasks found. Add your first task with: drawing-tasks add \"Task description\"")
            return 0
        
        # Sort tasks alphabetically (case-sensitive)
        sorted_tasks = sort_tasks(tasks)
        
        # Display tasks
        print("📝 Drawing Tasks:")
        for i, task in enumerate(sorted_tasks, 1):
            print(f"{i}. {task['description']}")
        
        return 0
        
    except json.JSONDecodeError as e:
        print(f"Error: Tasks file is corrupted. Cause: Invalid JSON format. Remediation: Backup and delete ~/.drawing-tasks/tasks.json to start fresh.", file=sys.stderr)
        return 1
    except PermissionError:
        print(f"Error: Cannot read tasks. Cause: Insufficient permissions. Remediation: Check file permissions for ~/.drawing-tasks/tasks.json", file=sys.stderr)
        return 1
    except Exception as e:
        print(f"Error: Cannot list tasks. Cause: {e}.", file=sys.stderr)
        return 1
