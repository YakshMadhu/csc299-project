"""Unit tests for file storage operations."""
import json
import pytest
from pathlib import Path
from src.storage.file_storage import load_tasks, save_tasks, get_storage_path


def test_load_tasks_empty_file(tmp_path):
    """Test loading tasks from an empty file."""
    # Create empty tasks file
    tasks_file = tmp_path / "tasks.json"
    tasks_file.write_text('{"tasks": []}')
    
    # Mock get_storage_path to return our test file
    import src.storage.file_storage as fs
    original_get_path = fs.get_storage_path
    fs.get_storage_path = lambda: tasks_file
    
    try:
        tasks = load_tasks()
        assert tasks == []
    finally:
        fs.get_storage_path = original_get_path


def test_load_tasks_valid_json(tmp_path):
    """Test loading tasks from valid JSON file."""
    tasks_file = tmp_path / "tasks.json"
    test_data = {
        "tasks": [
            {"description": "Draw a cat", "created_at": "2025-11-19T10:00:00Z"},
            {"description": "Draw a dog", "created_at": "2025-11-19T11:00:00Z"}
        ]
    }
    tasks_file.write_text(json.dumps(test_data))
    
    import src.storage.file_storage as fs
    original_get_path = fs.get_storage_path
    fs.get_storage_path = lambda: tasks_file
    
    try:
        tasks = load_tasks()
        assert len(tasks) == 2
        assert tasks[0]["description"] == "Draw a cat"
        assert tasks[1]["description"] == "Draw a dog"
    finally:
        fs.get_storage_path = original_get_path


def test_load_tasks_missing_file(tmp_path):
    """Test loading tasks when file doesn't exist."""
    tasks_file = tmp_path / "nonexistent.json"
    
    import src.storage.file_storage as fs
    original_get_path = fs.get_storage_path
    fs.get_storage_path = lambda: tasks_file
    
    try:
        tasks = load_tasks()
        assert tasks == []
    finally:
        fs.get_storage_path = original_get_path


def test_save_tasks_new_file(tmp_path):
    """Test saving tasks to a new file."""
    tasks_file = tmp_path / "tasks.json"
    test_tasks = [
        {"description": "Draw a cat", "created_at": "2025-11-19T10:00:00Z"}
    ]
    
    import src.storage.file_storage as fs
    original_get_path = fs.get_storage_path
    fs.get_storage_path = lambda: tasks_file
    
    try:
        save_tasks(test_tasks)
        
        # Verify file was created and contains correct data
        assert tasks_file.exists()
        data = json.loads(tasks_file.read_text())
        assert data["tasks"] == test_tasks
    finally:
        fs.get_storage_path = original_get_path


def test_save_tasks_overwrite_existing(tmp_path):
    """Test overwriting existing tasks file."""
    tasks_file = tmp_path / "tasks.json"
    old_data = {"tasks": [{"description": "Old task", "created_at": None}]}
    tasks_file.write_text(json.dumps(old_data))
    
    new_tasks = [
        {"description": "New task 1", "created_at": None},
        {"description": "New task 2", "created_at": None}
    ]
    
    import src.storage.file_storage as fs
    original_get_path = fs.get_storage_path
    fs.get_storage_path = lambda: tasks_file
    
    try:
        save_tasks(new_tasks)
        
        # Verify file was overwritten
        data = json.loads(tasks_file.read_text())
        assert len(data["tasks"]) == 2
        assert data["tasks"] == new_tasks
    finally:
        fs.get_storage_path = original_get_path


def test_load_tasks_corrupted_json(tmp_path):
    """Test loading tasks from corrupted JSON file."""
    tasks_file = tmp_path / "tasks.json"
    tasks_file.write_text('{"tasks": invalid json}')
    
    import src.storage.file_storage as fs
    original_get_path = fs.get_storage_path
    fs.get_storage_path = lambda: tasks_file
    
    try:
        with pytest.raises(json.JSONDecodeError):
            load_tasks()
    finally:
        fs.get_storage_path = original_get_path


def test_save_tasks_permission_error(tmp_path):
    """Test save_tasks() raises PermissionError when file is read-only."""
    tasks_file = tmp_path / "tasks.json"
    tasks_file.write_text('{"tasks": []}')
    
    # Make file read-only
    tasks_file.chmod(0o444)
    
    import src.storage.file_storage as fs
    original_get_path = fs.get_storage_path
    fs.get_storage_path = lambda: tasks_file
    
    try:
        test_tasks = [{"description": "Test task", "created_at": None}]
        with pytest.raises(PermissionError):
            save_tasks(test_tasks)
    finally:
        # Restore write permissions for cleanup
        tasks_file.chmod(0o644)
        fs.get_storage_path = original_get_path
