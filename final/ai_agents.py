# final/ai_agents.py
from __future__ import annotations
from typing import List

import openai  # pip install openai

from .config import OPENAI_API_KEY, OPENAI_MODEL
from .models import Note, Task
from .storage import load_notes, load_tasks


def _ensure_client() -> None:
    if not OPENAI_API_KEY:
        raise RuntimeError(
            "OPENAI_API_KEY is not set. Set it in your environment before using AI commands."
        )
    openai.api_key = OPENAI_API_KEY


def summarize_note_for_artist(note: Note) -> str:
    """
    Use the model to summarize a note into a short, actionable art tip.
    """
    _ensure_client()

    system_prompt = (
        "You are an art mentor helping someone improve. "
        "Given a note from their personal knowledge system, "
        "summarize it as a short, practical tip (1–3 sentences)."
    )
    user_prompt = f"Title: {note.title}\nContent:\n{note.content}"

    resp = openai.ChatCompletion.create(
        model=OPENAI_MODEL,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        temperature=0.4,
    )
    return resp.choices[0].message["content"].strip()


def suggest_practice_routine(user_input: str) -> str:
    """
    Suggest a practice routine based on user struggles + recent notes/tasks.
    """
    _ensure_client()

    notes: List[Note] = load_notes()
    tasks: List[Task] = load_tasks()

    notes_summary = "\n".join(
        f"- [{n.id}] {n.title} (tags: {', '.join(n.tags) if n.tags else '-'})"
        for n in notes[-10:]
    ) or "(no notes yet)"

    tasks_summary = "\n".join(
        f"- [{t.id}] ({t.status}/{t.priority}) [{t.category or '-'}] {t.title}"
        for t in tasks[-10:]
    ) or "(no tasks yet)"

    system_prompt = (
        "You are an experienced drawing teacher. "
        "Given the student's struggles and their recent notes and tasks, "
        "create a short numbered practice plan for today or the next few days. "
        "Each item should be a concrete exercise (e.g., '10 min gesture warmup')."
    )

    user_prompt = (
        f"Student struggles/goals:\n{user_input}\n\n"
        f"Recent notes:\n{notes_summary}\n\n"
        f"Recent tasks:\n{tasks_summary}"
    )

    resp = openai.ChatCompletion.create(
        model=OPENAI_MODEL,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        temperature=0.6,
    )
    return resp.choices[0].message["content"].strip()
