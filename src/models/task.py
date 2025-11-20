"""Task data model for drawing tasks."""
from dataclasses import dataclass
from typing import Optional


@dataclass
class Task:
    """Represents a drawing task.
    
    Attributes:
        description: The task description
        created_at: Optional ISO 8601 timestamp of when the task was created
    """
    description: str
    created_at: Optional[str] = None
    
    def to_dict(self) -> dict:
        """Convert task to dictionary format for JSON serialization."""
        return {
            "description": self.description,
            "created_at": self.created_at
        }
    
    @classmethod
    def from_dict(cls, data: dict) -> "Task":
        """Create a Task from dictionary data."""
        return cls(
            description=data["description"],
            created_at=data.get("created_at")
        )
