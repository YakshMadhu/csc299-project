# Drawing Tasks CLI

A command-line tool for managing a list of drawing tasks. Tasks are stored locally in a JSON file and displayed in alphabetical order.

## Features

✓ **Add tasks**: Quickly add drawing tasks to your list
✓ **List tasks**: View all tasks in alphabetical order (case-sensitive)
✓ **Local storage**: Tasks stored in `~/.drawing-tasks/tasks.json`
✓ **Clean separation**: CLI logic separate from storage layer

## Requirements

- Python 3.14 or higher
- `v` tool for dependency management

## Installation

1. **Initialize the project with `v`**:
   ```bash
   v init
   ```

2. **Install dependencies**:
   ```bash
   v install
   ```

3. **Verify installation**:
   ```bash
   python -m src.cli.main --help
   ```

## Usage

### Add a Task

Add a new drawing task to your list:

```bash
python -m src.cli.main add "Draw a cat"
```

**Output**:
```
✓ Task added: Draw a cat
```

### List All Tasks

Display all tasks in alphabetical order:

```bash
python -m src.cli.main list
```

**Output**:
```
📝 Drawing Tasks:
1. Draw a cat
2. Draw a dog
3. Draw a landscape
```

## Command Reference

| Command | Description | Example |
|---------|-------------|---------|
| `add <description>` | Add a new task | `python -m src.cli.main add "Draw a tree"` |
| `list` | List all tasks alphabetically | `python -m src.cli.main list` |

## Examples

See `specs/001-drawing-tasks-cli/quickstart.md` for detailed usage scenarios.

## Project Structure

```
.
├── src/
│   ├── cli/          # Command-line interface
│   │   ├── main.py   # Entry point
│   │   └── commands/ # Add and list commands
│   ├── storage/      # Data persistence layer
│   │   ├── file_storage.py
│   │   └── task_manager.py
│   └── models/       # Data models
│       └── task.py
├── tests/
│   ├── unit/         # Unit tests
│   └── integration/  # Integration tests
├── pyproject.toml    # Project metadata
└── v.mod             # v tool configuration
```

## Error Handling

The CLI provides clear error messages following this pattern:

```
Error: [brief summary]
Cause: [underlying cause]
Remediation: [how to fix it]
```

**Exit codes**:
- `0`: Success
- `1`: Error (validation, file I/O, etc.)

## Storage Location

Tasks are stored at:
- **Primary**: `~/.drawing-tasks/tasks.json`
- **Fallback**: `./tasks.json` (if home directory unavailable)

## Testing

Run the test suite:

```bash
pytest
```

Run with coverage:

```bash
pytest --cov=src --cov-report=term-missing
```

## Development

This project follows the principles defined in `.specify/memory/constitution.md`:

- **Code Clarity**: Self-documenting code with clear naming
- **Simplicity**: Minimal dependencies, straightforward architecture
- **Quality**: Type hints, error handling, atomic file writes
- **Testing**: Unit and integration tests with >80% coverage target
- **UX Consistency**: Emojis for feedback, clear error messages

## License

[License information here]
