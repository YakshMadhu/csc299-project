"""File storage operations for drawing tasks."""
import json
import os
from pathlib import Path
from typing import List, Dict, Any


def get_storage_path() -> Path:
    """Get the path to the tasks storage file.
    
    Returns:
        Path to ~/.drawing-tasks/tasks.json, or ./tasks.json as fallback
    """
    try:
        home_dir = Path.home()
        storage_dir = home_dir / ".drawing-tasks"
        storage_dir.mkdir(parents=True, exist_ok=True)
        return storage_dir / "tasks.json"
    except (OSError, RuntimeError):
        # Fallback to current directory if home directory is not accessible
        return Path("./tasks.json")


def load_tasks() -> List[Dict[str, Any]]:
    """Load tasks from the JSON storage file.
    
    Returns:
        List of task dictionaries
        
    Raises:
        json.JSONDecodeError: If the file contains invalid JSON
        OSError: If there are file system errors
    """
    storage_path = get_storage_path()
    
    if not storage_path.exists():
        return []
    
    try:
        with open(storage_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return data.get("tasks", [])
    except json.JSONDecodeError as e:
        raise json.JSONDecodeError(
            f"Tasks file is corrupted. {e.msg}",
            e.doc,
            e.pos
        )


def save_tasks(tasks: List[Dict[str, Any]]) -> None:
    """Save tasks to the JSON storage file using atomic write.
    
    Args:
        tasks: List of task dictionaries to save
        
    Raises:
        PermissionError: If the file cannot be written due to permissions
        OSError: If there are other file system errors
    """
    storage_path = get_storage_path()
    temp_path = storage_path.with_suffix('.tmp')
    
    data = {"tasks": tasks}
    
    try:
        # Write to temporary file first
        with open(temp_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        
        # Atomic rename
        temp_path.replace(storage_path)
    except PermissionError as e:
        # Clean up temp file if it exists
        if temp_path.exists():
            try:
                temp_path.unlink()
            except:
                pass
        raise PermissionError(f"Cannot save tasks: {e}")
    except OSError as e:
        # Clean up temp file if it exists
        if temp_path.exists():
            try:
                temp_path.unlink()
            except:
                pass
        raise OSError(f"Cannot save tasks: {e}")
