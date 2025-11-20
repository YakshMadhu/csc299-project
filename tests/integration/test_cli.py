"""Integration tests for CLI commands."""
import json
import subprocess
import sys
from pathlib import Path
import pytest


def test_add_command_creates_file(tmp_path, monkeypatch):
    """Test that add command creates a task file."""
    tasks_file = tmp_path / "tasks.json"
    
    # Mock get_storage_path
    import src.storage.file_storage as fs
    original_get_path = fs.get_storage_path
    fs.get_storage_path = lambda: tasks_file
    
    try:
        from src.cli.commands.add import add_task
        
        result = add_task("Draw a cat")
        
        assert result == 0
        assert tasks_file.exists()
        
        data = json.loads(tasks_file.read_text())
        assert len(data["tasks"]) == 1
        assert data["tasks"][0]["description"] == "Draw a cat"
    finally:
        fs.get_storage_path = original_get_path


def test_add_and_list_workflow(tmp_path):
    """Test adding multiple tasks and listing them in sorted order."""
    tasks_file = tmp_path / "tasks.json"
    
    import src.storage.file_storage as fs
    original_get_path = fs.get_storage_path
    fs.get_storage_path = lambda: tasks_file
    
    try:
        from src.cli.commands.add import add_task
        from src.cli.commands.list import list_tasks
        from io import StringIO
        
        # Add multiple tasks
        add_task("zebra")
        add_task("Apple")
        add_task("banana")
        
        # Capture list output
        old_stdout = sys.stdout
        sys.stdout = output = StringIO()
        
        try:
            result = list_tasks()
            output_text = output.getvalue()
        finally:
            sys.stdout = old_stdout
        
        assert result == 0
        # Verify alphabetical case-sensitive order
        assert "Apple" in output_text
        assert "banana" in output_text
        assert "zebra" in output_text
        
        # Check order (Apple should appear before banana)
        apple_pos = output_text.index("Apple")
        banana_pos = output_text.index("banana")
        zebra_pos = output_text.index("zebra")
        assert apple_pos < banana_pos < zebra_pos
        
    finally:
        fs.get_storage_path = original_get_path


def test_add_empty_task_fails(tmp_path):
    """Test that adding an empty task returns an error."""
    tasks_file = tmp_path / "tasks.json"
    
    import src.storage.file_storage as fs
    original_get_path = fs.get_storage_path
    fs.get_storage_path = lambda: tasks_file
    
    try:
        from src.cli.commands.add import add_task
        
        result = add_task("")
        assert result == 1
        
        result = add_task("   ")
        assert result == 1
    finally:
        fs.get_storage_path = original_get_path


def test_list_empty_tasks(tmp_path):
    """Test listing when no tasks exist."""
    tasks_file = tmp_path / "tasks.json"
    
    import src.storage.file_storage as fs
    original_get_path = fs.get_storage_path
    fs.get_storage_path = lambda: tasks_file
    
    try:
        from src.cli.commands.list import list_tasks
        from io import StringIO
        
        old_stdout = sys.stdout
        sys.stdout = output = StringIO()
        
        try:
            result = list_tasks()
            output_text = output.getvalue()
        finally:
            sys.stdout = old_stdout
        
        assert result == 0
        assert "No tasks found" in output_text or output_text.strip() == ""
    finally:
        fs.get_storage_path = original_get_path


def test_add_command_permission_error(tmp_path):
    """Test add command handles file permission errors gracefully."""
    tasks_file = tmp_path / "tasks.json"
    tasks_file.write_text('{"tasks": []}')
    tasks_file.chmod(0o444)  # Read-only
    
    import src.storage.file_storage as fs
    original_get_path = fs.get_storage_path
    fs.get_storage_path = lambda: tasks_file
    
    try:
        from src.cli.commands.add import add_task
        from io import StringIO
        
        old_stderr = sys.stderr
        sys.stderr = output = StringIO()
        
        try:
            result = add_task("Test task")
            error_text = output.getvalue()
        finally:
            sys.stderr = old_stderr
        
        assert result == 1
        assert "Error" in error_text or "Permission" in error_text
    finally:
        tasks_file.chmod(0o644)
        fs.get_storage_path = original_get_path


def test_list_command_corrupted_json(tmp_path):
    """Test list command handles corrupted storage file gracefully."""
    tasks_file = tmp_path / "tasks.json"
    tasks_file.write_text('{"tasks": invalid json content}')
    
    import src.storage.file_storage as fs
    original_get_path = fs.get_storage_path
    fs.get_storage_path = lambda: tasks_file
    
    try:
        from src.cli.commands.list import list_tasks
        from io import StringIO
        
        old_stderr = sys.stderr
        sys.stderr = output = StringIO()
        
        try:
            result = list_tasks()
            error_text = output.getvalue()
        finally:
            sys.stderr = old_stderr
        
        assert result == 1
        assert "Error" in error_text or "corrupted" in error_text.lower()
    finally:
        fs.get_storage_path = original_get_path
