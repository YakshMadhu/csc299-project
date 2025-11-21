# final/storage.py
from __future__ import annotations
import json
from pathlib import Path
from typing import List, Dict, Any
from .models import now_iso


from .models import Note, Task

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
NOTES_FILE = DATA_DIR / "notes.json"
TASKS_FILE = DATA_DIR / "tasks.json"
LOG_DIR = BASE_DIR / "logs"
LOG_FILE = LOG_DIR / "commands.log"



def _ensure_data_dir() -> None:
    DATA_DIR.mkdir(parents=True, exist_ok=True)


def _load_json(path: Path) -> Dict[str, Any]:
    if not path.exists():
        return {}
    try:
        with path.open("r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return {}


def _save_json(path: Path, data: Dict[str, Any]) -> None:
    with path.open("w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


# ---------- Notes ----------

def load_notes() -> List[Note]:
    _ensure_data_dir()
    raw = _load_json(NOTES_FILE)
    items = raw.get("notes", [])
    return [Note.from_dict(d) for d in items]


def save_notes(notes: List[Note]) -> None:
    _ensure_data_dir()
    data = {"notes": [n.to_dict() for n in notes]}
    _save_json(NOTES_FILE, data)


def next_note_id(notes: List[Note]) -> int:
    return max((n.id for n in notes), default=0) + 1


# ---------- Tasks ----------

def load_tasks() -> List[Task]:
    _ensure_data_dir()
    raw = _load_json(TASKS_FILE)
    items = raw.get("tasks", [])
    return [Task.from_dict(d) for d in items]


def save_tasks(tasks: List[Task]) -> None:
    _ensure_data_dir()
    data = {"tasks": [t.to_dict() for t in tasks]}
    _save_json(TASKS_FILE, data)


def next_task_id(tasks: List[Task]) -> int:
    return max((t.id for t in tasks), default=0) + 1

def log_command(command: str) -> None:
    LOG_DIR.mkdir(parents=True, exist_ok=True)
    timestamp = now_iso()
    with LOG_FILE.open("a", encoding="utf-8") as f:
        f.write(f"[{timestamp}] {command}\n")
