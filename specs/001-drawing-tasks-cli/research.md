# Research Notes: Drawing Tasks CLI

**Feature**: Drawing Tasks CLI
**Phase**: 0 - Research
**Date**: 2025-11-19

## Technology Selection

### CLI Framework
- **Choice**: argparse (built-in)
- **Rationale**: Built-in to Python, simple API, well-documented
- **Alternatives considered**: click (additional dependency), typer (requires pydantic)

### Storage Format
- **Choice**: JSON
- **Rationale**: Human-readable, built-in Python support, simple schema
- **Alternatives considered**: CSV (harder to extend), SQLite (overkill for scope)

### Language & Runtime
- **Choice**: Python 3.14+
- **Rationale**: Simple syntax, cross-platform, strong standard library
- **Dependency Management**: 'v' tool for initialization and script running
- **Alternatives considered**: Node.js/TypeScript (more complex setup), Go (requires compilation)

## File Storage Strategy

### Location
- Default: `~/.drawing-tasks/tasks.json` (user home directory)
- Fallback: `./tasks.json` (current directory if home not accessible)

### File Format
```json
{
  "tasks": [
    {"description": "Draw a cat", "createdAt": "2025-11-19T10:30:00Z"},
    {"description": "Draw a dog", "createdAt": "2025-11-19T11:00:00Z"}
  ]
}
```

### Concurrency Handling
- Use file locking or atomic write pattern (write to temp file, rename)
- Read entire file, modify in memory, write atomically
- For MVP: simple error message if file is locked/busy

## Alphabetical Sorting

### Implementation
- Case-sensitive sort using Python's default string comparison
- Sort happens during list operation (storage remains insertion-ordered)
- Example: "Apple" < "Zebra" < "apple" < "zebra"

```python
tasks.sort(key=lambda t: t['description'])
```

## Error Handling Strategy

### File Errors
- Permission denied → "Error: Cannot access tasks file. Cause: Insufficient permissions. Remediation: Check file permissions or run with appropriate access."
- Disk full → "Error: Cannot save task. Cause: Disk is full. Remediation: Free up disk space."
- Corrupted file → "Error: Tasks file is corrupted. Cause: Invalid JSON format. Remediation: Backup and delete ~/.drawing-tasks/tasks.json to start fresh."

### Validation
- Empty task description → reject with error
- Task description > 500 chars → warn or truncate (to be clarified)

## Testing Approach

### Unit Tests
- Storage: `load_tasks()`, `save_tasks()`, `sort_tasks()`
- Use pytest with fixtures and tmp_path for file system isolation

### Integration Tests
- Full CLI workflow: add task → list tasks → verify output
- Use subprocess to invoke CLI, assert on stdout/stderr
- Use temporary directory for test isolation

## Open Questions

None - all requirements are clear from spec.
