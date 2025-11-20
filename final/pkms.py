# final/pkms.py
from __future__ import annotations
from typing import List, Optional

from .models import Note
from .storage import load_notes, save_notes, next_note_id


def add_note_interactive() -> Note:
    notes = load_notes()
    nid = next_note_id(notes)

    print(">>> Creating a new note")
    title = input("Title: ").strip()
    print("Content (finish with an empty line):")
    lines: List[str] = []
    while True:
        line = input()
        if not line.strip():
            break
        lines.append(line)
    content = "\n".join(lines)

    tags_str = input("Tags (comma-separated, e.g., anatomy, gesture): ").strip()
    tags = [t.strip() for t in tags_str.split(",")] if tags_str else []

    note = Note.create(nid, title, content, tags)
    notes.append(note)
    save_notes(notes)

    print(f"Saved note #{note.id}")
    return note


def list_notes() -> None:
    notes = load_notes()
    if not notes:
        print("No notes yet. Add one with `add-note`.")
        return
    print("Your notes:")
    for n in notes:
        tags_str = ", ".join(n.tags) if n.tags else "-"
        print(f"- [{n.id}] {n.title} (tags: {tags_str}, updated: {n.updated_at})")


def find_note_by_id(note_id: int) -> Optional[Note]:
    notes = load_notes()
    for n in notes:
        if n.id == note_id:
            return n
    return None


def view_note(note_id: int) -> None:
    n = find_note_by_id(note_id)
    if not n:
        print(f"No note found with id {note_id}")
        return
    print("=" * 40)
    print(f"Note #{n.id}: {n.title}")
    if n.tags:
        print(f"Tags: {', '.join(n.tags)}")
    print(f"Created: {n.created_at}")
    print(f"Updated: {n.updated_at}")
    print("-" * 40)
    print(n.content)
    print("=" * 40)


def search_notes(query: str) -> None:
    query = query.lower().strip()
    notes = load_notes()
    matches = [
        n for n in notes
        if query in n.title.lower()
        or query in n.content.lower()
        or any(query in t.lower() for t in n.tags)
    ]
    if not matches:
        print(f"No notes matched '{query}'.")
        return
    print(f"Notes matching '{query}':")
    for n in matches:
        tags_str = ", ".join(n.tags) if n.tags else "-"
        print(f"- [{n.id}] {n.title} (tags: {tags_str})")
