# final/ai_agents.py
from __future__ import annotations
from typing import List
from openai import OpenAI   # NEW SDK

from .config import OPENAI_API_KEY, OPENAI_MODEL
from .models import Note, Task
from .storage import load_notes, load_tasks

client = OpenAI(api_key=OPENAI_API_KEY)


def summarize_note_for_artist(note: Note) -> str:
    """
    Use the model to summarize a note into a short, actionable art tip.
    """
    system_prompt = (
        "You are an art mentor helping someone improve. "
        "Summarize the following note into a short practical tip (1–3 sentences)."
    )

    user_prompt = f"Title: {note.title}\nContent:\n{note.content}"

    resp = client.chat.completions.create(
        model=OPENAI_MODEL,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        temperature=0.4
    )

    return resp.choices[0].message.content.strip()


def suggest_practice_routine(user_input: str) -> str:
    """
    Suggest a practice routine based on user struggles + recent notes/tasks.
    """
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
        "Given the student's struggles and their recent notes/tasks, "
        "create a short numbered practice plan (3–7 steps)."
    )

    user_prompt = (
        f"Struggles/goals:\n{user_input}\n\n"
        f"Recent notes:\n{notes_summary}\n\n"
        f"Recent tasks:\n{tasks_summary}"
    )

    resp = client.chat.completions.create(
        model=OPENAI_MODEL,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        temperature=0.6
    )

    return resp.choices[0].message.content.strip()


def analyze_task_ai(title: str, description: str) -> dict:
    """
    AI reads a task title + description and returns JSON:
    {priority, category, due_date, tip}
    """

    system_prompt = (
        "Return ONLY valid JSON. Do not include any explanation, comments, or text before or after.\n"
        "Format must be exactly:\n"
        "{\n"
        "  \"priority\": \"low|medium|high\",\n"
        "  \"category\": \"string or null\",\n"
        "  \"due_date\": \"YYYY-MM-DD or null\",\n"
        "  \"tip\": \"string\"\n"
        "}"
    )

    user_prompt = f"Title: {title}\nDescription: {description}"

    resp = client.chat.completions.create(
        model=OPENAI_MODEL,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        temperature=0.2
    )

    import json
    raw = resp.choices[0].message.content.strip()

    try:
        # Some models wrap JSON in ```json ... ```
        if raw.startswith("```"):
            raw = raw.strip("`").replace("json", "").strip()

        parsed = json.loads(raw)
        return parsed

    except Exception as e:
        print("JSON parse error:", e, "\nRaw AI output:", raw)
        return {
            "priority": "medium",
            "category": None,
            "due_date": None,
            "tip": "(AI response could not be parsed.)"
        }
