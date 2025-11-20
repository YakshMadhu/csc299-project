# CLI Module Documentation

## Overview

The CLI module provides the command-line interface for the Drawing Tasks application. It uses Python's `argparse` module to parse commands and route them to appropriate handlers.

## Structure

```
cli/
├── __init__.py
├── main.py           # CLI entry point and argument parsing
└── commands/
    ├── __init__.py
    ├── add.py        # Add command handler
    └── list.py       # List command handler
```

## Main Entry Point

**File**: `main.py`

The main entry point sets up the argument parser with two subcommands:
- `add`: Add a new drawing task
- `list`: List all drawing tasks

## Commands

### Add Command

**File**: `commands/add.py`

**Function**: `add_task(description: str) -> int`

Adds a new drawing task to the storage file.

**Arguments**:
- `description`: Task description string

**Returns**:
- `0` on success
- `1` on error

**Validation**:
- Rejects empty or whitespace-only descriptions

**Error Handling**:
- Permission errors when writing to file
- OS errors (disk full, etc.)
- Generic exceptions

### List Command

**File**: `commands/list.py`

**Function**: `list_tasks() -> int`

Lists all drawing tasks in alphabetical order (case-sensitive).

**Returns**:
- `0` on success
- `1` on error

**Behavior**:
- Displays tasks sorted alphabetically (case-sensitive)
- Shows numbered list with emoji prefix (📝)
- Shows friendly message if no tasks exist

**Error Handling**:
- JSON decode errors (corrupted file)
- Permission errors when reading file
- Generic exceptions

## Usage

### As Module

```python
from src.cli.main import main
import sys

sys.exit(main())
```

### As Installed Command

```bash
drawing-tasks add "Draw a cat"
drawing-tasks list
```

## Exit Codes

- `0`: Success
- `1`: Error occurred

## Dependencies

- `argparse` (built-in): Command-line argument parsing
- `src.storage.file_storage`: File I/O operations
- `src.storage.task_manager`: Task sorting
