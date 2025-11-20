# Data Model: Drawing Tasks CLI

**Feature**: Drawing Tasks CLI
**Phase**: 1 - Design
**Date**: 2025-11-19

## Entities

### Task

Represents a single drawing task.

**Attributes**:
- `description` (string, required): The task description entered by the user
- `createdAt` (ISO 8601 timestamp, optional): When the task was created (for future extension)

**Constraints**:
- `description` must not be empty
- `description` length: 1-500 characters (recommended)
- `createdAt` format: ISO 8601 (e.g., "2025-11-19T10:30:00Z")

**Example**:
```python
from dataclasses import dataclass
from typing import Optional
from datetime import datetime

@dataclass
class Task:
    description: str
    created_at: Optional[str] = None  # ISO 8601 timestamp
```

## Storage Schema

### File Format: JSON

**Location**: `~/.drawing-tasks/tasks.json`

**Schema**:
```json
{
  "tasks": [
    {
      "description": "Draw a cat",
      "createdAt": "2025-11-19T10:30:00Z"
    },
    {
      "description": "Draw a dog",
      "createdAt": "2025-11-19T11:00:00Z"
    }
  ]
}
```

**Notes**:
- Tasks array is stored in insertion order
- Sorting to alphabetical order happens at display time, not in storage
- Empty file or missing file is treated as empty task list

## Sorting Rules

Tasks are displayed in **case-sensitive alphabetical order**:
- Uppercase letters come before lowercase in ASCII ordering
- Example order: "Apple", "Zebra", "apple", "banana", "zebra"

**Implementation**:
```python
tasks.sort(key=lambda t: t['description'])
```

## Future Extensions (Not in Scope)

- Task ID (for deletion/editing)
- Priority field
- Due date
- Completion status
- Tags or categories
