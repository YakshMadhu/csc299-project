# final/ai_agents.py
from __future__ import annotations
from typing import List
from openai import OpenAI
from datetime import datetime, timedelta
import json

from .config import OPENAI_API_KEY, OPENAI_MODEL
from .models import Note, Task
from .storage import load_notes, load_tasks

client = OpenAI(api_key=OPENAI_API_KEY)


# ------------------------------------------------------
# SUMMARIZE NOTE
# ------------------------------------------------------
def summarize_note_for_artist(note: Note) -> str:
    system_prompt = (
        "You are an advanced art mentor. Summarize the student's note into "
        "a short, practical artistic tip (1–3 sentences)."
    )

    user_prompt = f"Title: {note.title}\nContent:\n{note.content}"

    resp = client.chat.completions.create(
        model=OPENAI_MODEL,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        temperature=0.4,
    )
    return resp.choices[0].message.content.strip()


# ------------------------------------------------------
# PRACTICE ROUTINE
# ------------------------------------------------------
def suggest_practice_routine(user_input: str) -> str:
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
        "You are an expert drawing instructor. Based on the student's struggles, "
        "recent notes, and tasks, create a practice routine with 3–7 concrete steps."
    )

    user_prompt = (
        f"Student struggles:\n{user_input}\n\n"
        f"Recent notes:\n{notes_summary}\n\n"
        f"Recent tasks:\n{tasks_summary}"
    )

    resp = client.chat.completions.create(
        model=OPENAI_MODEL,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        temperature=0.6,
    )

    return resp.choices[0].message.content.strip()


# ------------------------------------------------------
# TASK ANALYSIS (AI FEATURE — PROTOTYPE 3)
# ------------------------------------------------------
def analyze_task_ai(title: str, description: str) -> dict:
    today = datetime.today().strftime("%Y-%m-%d")

    system_prompt = f"""
You are a world-class professional art instructor and curriculum designer.

Your job is to analyze the TITLE and DESCRIPTION of a task and produce a thoughtful,
expert-level output.

You MUST return a strict JSON object with:
{{
  "priority": "high" | "medium" | "low",
  "category": "A short, real-time, expert-generated category label (NOT chosen from a fixed list)",
  "due_date": "YYYY-MM-DD" | null,
  "tip": "A detailed, highly professional art instruction (3–6 sentences)."
}}

–––––––––––––––––––––––––––
RULES
–––––––––––––––––––––––––––

1. CATEGORY:
   • Must be generated dynamically based on the title & description.
   • Examples (but DO NOT restrict to these): "Anatomy – Hips", "Portrait Construction",
     "Gesture Flow", "Realistic Rendering", "3D Form Design", "Structural Drawing",
     "Cloth Study", "Lighting & Shadow Logic", "Color Harmony", etc.
   • Create a category that a real art mentor would use to classify the task.

2. PRIORITY:
   • high → core art fundamentals (anatomy, gesture, head/figure, perspective)
   • medium → useful improvement studies (rendering, color, stylization)
   • low → optional explorations / experimental tasks

3. DUE DATE:
   Today is {today}.
   • high → today + 1 day
   • medium → today + 3 days
   • low → today + 5–7 days

4. TIP STYLE:
   • Must sound like a top-tier art teacher giving a masterclass.
   • No generic filler.
   • Must include actionable, technical, step-by-step guidance.
   • Must be specific to the EXACT task in title/description.

5. OUTPUT FORMAT:
   • You MUST output ONLY a JSON object with no extra text anywhere.
"""

    user_prompt = f"""
TITLE: {title}
DESCRIPTION: {description}

Return ONLY the JSON object. No commentary.
"""

    resp = client.chat.completions.create(
        model=OPENAI_MODEL,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        temperature=0.3,  # Lower for JSON stability
    )

    raw = resp.choices[0].message.content.strip()

    # Parse JSON safely
    try:
        return json.loads(raw)
    except Exception:
        # Strong fallback instruction instead of generic 3D shapes
        return {
            "priority": "medium",
            "category": "General Artistic Study",
            "due_date": (datetime.today() + timedelta(days=3)).strftime("%Y-%m-%d"),
            "tip": (
                "Begin by simplifying the subject into larger structural forms, then build up "
                "anatomical accuracy using observed references. Focus on proportion, rhythm, and "
                "perspective before refining the details. Always construct the form in 3D and rotate "
                "it mentally to deepen understanding."
            )
        }

