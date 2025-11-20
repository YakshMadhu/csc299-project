"""Unit tests for task manager operations."""
import pytest
from src.storage.task_manager import sort_tasks


def test_sort_tasks_case_sensitive():
    """Test that tasks are sorted alphabetically with case-sensitivity."""
    tasks = [
        {"description": "zebra", "created_at": None},
        {"description": "Apple", "created_at": None},
        {"description": "banana", "created_at": None},
        {"description": "Zebra", "created_at": None}
    ]
    
    sorted_tasks = sort_tasks(tasks)
    
    # Case-sensitive alphabetical order: uppercase before lowercase
    descriptions = [t["description"] for t in sorted_tasks]
    assert descriptions == ["Apple", "Zebra", "banana", "zebra"]


def test_sort_tasks_empty_list():
    """Test sorting an empty list of tasks."""
    tasks = []
    sorted_tasks = sort_tasks(tasks)
    assert sorted_tasks == []


def test_sort_tasks_single_task():
    """Test sorting a single task."""
    tasks = [{"description": "Only task", "created_at": None}]
    sorted_tasks = sort_tasks(tasks)
    assert len(sorted_tasks) == 1
    assert sorted_tasks[0]["description"] == "Only task"


def test_sort_tasks_already_sorted():
    """Test sorting tasks that are already in order."""
    tasks = [
        {"description": "Apple", "created_at": None},
        {"description": "Banana", "created_at": None},
        {"description": "Cherry", "created_at": None}
    ]
    
    sorted_tasks = sort_tasks(tasks)
    descriptions = [t["description"] for t in sorted_tasks]
    assert descriptions == ["Apple", "Banana", "Cherry"]
