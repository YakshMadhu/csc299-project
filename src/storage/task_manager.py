"""Task management operations including sorting."""
from typing import List, Dict, Any


def sort_tasks(tasks: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Sort tasks alphabetically by description (case-sensitive).
    
    Args:
        tasks: List of task dictionaries
        
    Returns:
        Sorted list of tasks. Uppercase letters come before lowercase.
        Example order: "Apple", "Zebra", "apple", "banana", "zebra"
    """
    return sorted(tasks, key=lambda t: t['description'])
