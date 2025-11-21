
from __future__ import annotations
from dataclasses import dataclass, asdict
from datetime import datetime
from typing import List, Optional, Dict, Any


def now_iso() -> str:
    return datetime.now().isoformat(timespec="seconds")


@dataclass
class Note:
    id: int
    title: str
    content: str
    tags: List[str]
    created_at: str
    updated_at: str

    @classmethod
    def create(cls, note_id: int, title: str, content: str, tags: List[str]) -> "Note":
        ts = now_iso()
        clean_tags = [t.strip() for t in tags if t.strip()]
        return cls(
            id=note_id,
            title=title.strip(),
            content=content.strip(),
            tags=clean_tags,
            created_at=ts,
            updated_at=ts,
        )

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Note":
        return cls(
            id=data["id"],
            title=data["title"],
            content=data["content"],
            tags=data.get("tags", []),
            created_at=data.get("created_at", now_iso()),
            updated_at=data.get("updated_at", now_iso()),
        )


@dataclass
class Task:
    id: int
    title: str
    description: str
    priority: str
    status: str         # todo | in-progress | done
    category: Optional[str]
    due_date: Optional[str]
    created_at: str
    completed_at: Optional[str]
    updated_at: str = ""

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)

    @classmethod
    def create(
        cls,
        task_id: int,
        title: str,
        description: str,
        priority: str = "medium",
        category: Optional[str] = None,
        due_date: Optional[str] = None,
    ) -> "Task":
        ts = now_iso()
        priority = (priority or "medium").lower().strip()
        if priority not in ("low", "medium", "high"):
            priority = "medium"

        return cls(
            id=task_id,
            title=title.strip(),
            description=description.strip(),
            priority=priority,
            status="todo",
            category=category.strip() if category else None,
            due_date=due_date.strip() if due_date else None,
            created_at=ts,
            completed_at=None,
            updated_at=ts,
        )

    def mark_in_progress(self) -> None:
        self.status = "in-progress"
        self.updated_at = now_iso()

    def mark_done(self) -> None:
        self.status = "done"
        self.completed_at = now_iso()
        self.updated_at = now_iso()

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Task":
        return cls(
            id=data["id"],
            title=data["title"],
            description=data.get("description", ""),
            priority=data.get("priority", "medium"),
            status=data.get("status", "todo"),
            category=data.get("category"),
            due_date=data.get("due_date"),
            created_at=data.get("created_at", now_iso()),
            completed_at=data.get("completed_at"),
            updated_at=data.get("updated_at", now_iso()),
        )
