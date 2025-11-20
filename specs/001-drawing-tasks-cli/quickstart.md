# Quickstart: Drawing Tasks CLI

**Feature**: Drawing Tasks CLI
**Last Updated**: 2025-11-19

## Installation

```bash
# Initialize project with 'v' (if not already done)
v init

# Install dependencies
v install

# Make CLI executable (optional - adds to PATH)
v run install-cli
```

## Usage

### Add a Task

```bash
# Add a new drawing task
python -m src.cli.main add "Draw a cat"
python -m src.cli.main add "Paint a landscape"
python -m src.cli.main add "Sketch a portrait"

# Or if installed globally:
drawing-tasks add "Draw a cat"
```

**Expected Output**:
```
✓ Task added: Draw a cat
```

### List All Tasks

```bash
# List all tasks (alphabetically sorted, case-sensitive)
python -m src.cli.main list

# Or if installed globally:
drawing-tasks list
```

**Expected Output**:
```
📝 Drawing Tasks:
1. Draw a cat
2. Paint a landscape
3. Sketch a portrait
```

**Note**: Tasks are displayed in case-sensitive alphabetical order. For example, "Apple" appears before "banana".

### Alphabetical Sorting Example

```bash
python -m src.cli.main add "zebra"
python -m src.cli.main add "Apple"
python -m src.cli.main add "banana"
python -m src.cli.main list
```

**Expected Output**:
```
📝 Drawing Tasks:
1. Apple
2. banana
3. zebra
```

## Error Handling

### Empty Task
```bash
python -m src.cli.main add ""
```
**Output**:
```
Error: Task description cannot be empty
Cause: No description provided
Remediation: Please provide a valid task description
```

### File Permission Error
```bash
# If ~/.drawing-tasks/tasks.json is read-only
python -m src.cli.main add "New task"
```
**Output**:
```
Error: Failed to save tasks
Cause: Permission denied
Remediation: Check file permissions for ~/.drawing-tasks/tasks.json
```

### Corrupted Storage File
```bash
# If ~/.drawing-tasks/tasks.json contains invalid JSON
python -m src.cli.main list
```
**Output**:
```
Error: Tasks file is corrupted
Cause: Invalid JSON format
Remediation: Backup and delete ~/.drawing-tasks/tasks.json to start fresh
```

## Development

### Run Tests

```bash
# Run all tests
v run test

# Or use pytest directly
pytest

# Run unit tests only
pytest tests/unit/

# Run integration tests only
pytest tests/integration/

# Run with coverage
pytest --cov=src --cov-report=html
```

### Linting and Formatting

```bash
# Lint code (if configured)
v run lint

# Format code (if using black/ruff)
v run format
```

## Storage Location

Tasks are stored in: `~/.drawing-tasks/tasks.json`

To view or manually edit the file:
```bash
cat ~/.drawing-tasks/tasks.json
```

## Troubleshooting

**Q: Tasks are not persisting**
- Check file permissions for `~/.drawing-tasks/`
- Verify disk space is available

**Q: Tasks appear in wrong order**
- Verify you're using the `list` command (not viewing the raw file)
- Remember: sorting is case-sensitive ("A" before "a")

**Q: Command not found**
- Use `python -m src.cli.main` instead
- Or run `v run install-cli` to make globally available
