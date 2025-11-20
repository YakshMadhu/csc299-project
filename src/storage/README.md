# Storage Module Documentation

## Overview

The storage module handles persistent storage of drawing tasks using JSON files. It provides clean separation between file I/O operations and CLI logic, ensuring maintainability and testability.

## Structure

```
storage/
├── __init__.py
├── file_storage.py    # File I/O operations
└── task_manager.py    # Task sorting and management
```

## Modules

### File Storage

**File**: `file_storage.py`

Handles reading and writing task data to/from JSON files.

#### Functions

**`get_storage_path() -> Path`**

Returns the path to the tasks storage file.

**Behavior**:
- Primary location: `~/.drawing-tasks/tasks.json`
- Fallback location: `./tasks.json` (if home directory is not accessible)
- Creates directory if it doesn't exist

**Returns**: `pathlib.Path` object

---

**`load_tasks() -> List[Dict[str, Any]]`**

Loads tasks from the JSON storage file.

**Returns**: List of task dictionaries

**Behavior**:
- Returns empty list if file doesn't exist
- Parses JSON and extracts `tasks` array

**Raises**:
- `json.JSONDecodeError`: If file contains invalid JSON
- `OSError`: On file system errors

---

**`save_tasks(tasks: List[Dict[str, Any]]) -> None`**

Saves tasks to the JSON storage file using atomic write pattern.

**Arguments**:
- `tasks`: List of task dictionaries

**Behavior**:
- Writes to temporary file first (`.tmp` suffix)
- Atomically renames temp file to final location
- Cleans up temp file on error

**Raises**:
- `PermissionError`: If file cannot be written
- `OSError`: On other file system errors

**Atomic Write Pattern**:
1. Write data to `tasks.tmp`
2. Rename `tasks.tmp` → `tasks.json` (atomic operation)
3. Ensures data integrity even if process is interrupted

### Task Manager

**File**: `task_manager.py`

Provides task manipulation operations.

#### Functions

**`sort_tasks(tasks: List[Dict[str, Any]]) -> List[Dict[str, Any]]`**

Sorts tasks alphabetically by description (case-sensitive).

**Arguments**:
- `tasks`: List of task dictionaries

**Returns**: New sorted list of tasks

**Sorting Behavior**:
- Case-sensitive alphabetical order
- Uppercase letters come before lowercase
- Example order: "Apple", "Zebra", "apple", "banana", "zebra"

## Storage Format

### JSON Structure

```json
{
  "tasks": [
    {
      "description": "Draw a cat",
      "created_at": "2025-11-19T10:30:00Z"
    },
    {
      "description": "Draw a dog",
      "created_at": "2025-11-19T11:00:00Z"
    }
  ]
}
```

### Task Dictionary

Each task is a dictionary with:
- `description` (str, required): Task description
- `created_at` (str, optional): ISO 8601 timestamp

## Design Principles

### Separation of Concerns

- File I/O is isolated in `file_storage.py`
- Business logic (sorting) is in `task_manager.py`
- No CLI logic in storage module

### Data Integrity

- Atomic writes prevent data corruption
- Proper error handling with specific exceptions
- Temp file cleanup on errors

### Testability

- Functions are pure and side-effect free (except I/O)
- Easy to mock file paths for testing
- Clear function contracts

## Usage Examples

### Loading and Saving

```python
from src.storage.file_storage import load_tasks, save_tasks

# Load existing tasks
tasks = load_tasks()

# Add a new task
new_task = {
    "description": "Draw a landscape",
    "created_at": "2025-11-19T12:00:00Z"
}
tasks.append(new_task)

# Save back to file
save_tasks(tasks)
```

### Sorting Tasks

```python
from src.storage.task_manager import sort_tasks

tasks = [
    {"description": "zebra", "created_at": None},
    {"description": "Apple", "created_at": None}
]

sorted_tasks = sort_tasks(tasks)
# Result: [{"description": "Apple", ...}, {"description": "zebra", ...}]
```

## Dependencies

- `json` (built-in): JSON parsing and serialization
- `pathlib` (built-in): Path manipulation
- `typing` (built-in): Type hints
