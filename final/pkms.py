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

def edit_note_interactive(note_id: int) -> None:
    notes = load_notes()
    target = None
    for n in notes:
        if n.id == note_id:
            target = n
            break

    if not target:
        print(f"No note found with id {note_id}")
        return

    print(f"Editing Note #{note_id}")
    print("Leave any field blank to keep the current value.\n")

    # --- Title ---
    print(f"Current title: {target.title}")
    new_title = input("New title: ").strip()
    if new_title:
        target.title = new_title

    # --- Content ---
    print("\nCurrent content:")
    print(target.content)
    print("\nEnter new content (end with empty line). Leave empty to keep existing:")
    new_lines = []
    while True:
        line = input()
        if not line.strip():
            break
        new_lines.append(line)

    if new_lines:
        target.content = "\n".join(new_lines)

    # --- Tags ---
    print(f"\nCurrent tags: {', '.join(target.tags) if target.tags else '-'}")
    new_tags = input("New tags (comma-separated): ").strip()
    if new_tags:
        target.tags = [t.strip() for t in new_tags.split(",") if t.strip()]

    # --- Update timestamp ---
    from .models import now_iso
    target.updated_at = now_iso()

    # --- Save changes ---
    save_notes(notes)
    print(f"\n✔ Note #{note_id} updated successfully!")



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

def filter_notes_by_tag(tag: str) -> None:
    tag = tag.lower().strip()
    notes = load_notes()

    matches = [
        n for n in notes
        if any(tag == t.lower() for t in n.tags)
    ]

    if not matches:
        print(f"No notes found with tag '{tag}'.")
        return

    print(f"Notes with tag '{tag}':")
    for n in matches:
        tags_str = ", ".join(n.tags) if n.tags else "-"
        print(f"- [{n.id}] {n.title} (tags: {tags_str})")
