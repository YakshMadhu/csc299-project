"""Add command handler."""
import sys
from datetime import datetime, UTC
from src.storage import load_tasks, save_tasks


def add_task(description: str) -> int:
    """Add a new drawing task.
    
    Args:
        description: Task description
        
    Returns:
        Exit code (0 for success, 1 for error)
    """
    # Validate description
    if not description or not description.strip():
        print("Error: Task description cannot be empty. Please provide a valid task description.", file=sys.stderr)
        return 1
    
    try:
        # Load existing tasks
        tasks = load_tasks()
        
        # Create new task
        new_task = {
            "description": description.strip(),
            "created_at": datetime.now(UTC).isoformat()
        }
        
        # Add to list
        tasks.append(new_task)
        
        # Save
        save_tasks(tasks)
        
        print(f"✓ Task added: \"{description.strip()}\"")
        return 0
        
    except PermissionError as e:
        print(f"Error: Cannot save task. Cause: Insufficient permissions. Remediation: Check file permissions for the tasks file.", file=sys.stderr)
        return 1
    except OSError as e:
        print(f"Error: Cannot save task. Cause: {e}. Remediation: Check disk space and file permissions.", file=sys.stderr)
        return 1
    except Exception as e:
        print(f"Error: Cannot save task. Cause: {e}.", file=sys.stderr)
        return 1
