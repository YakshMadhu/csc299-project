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

def generate_practices_from_task(task: Task) -> str:
    today = datetime.today().strftime("%Y-%m-%d")

    system_prompt = f"""
You are a world-class atelier art instructor (like Vilppu, Steve Huston, Proko, Watts Atelier instructors).

Your goal:
From ONE task (title + description + priority + category), generate **4–6 extremely effective practice drills** that a real teacher would give to build mastery.

Your drills must:
- feel like real assignments from a serious atelier program
- target the EXACT topic of the task (e.g., toes, forearms, hips, eyes)
- strengthen fundamentals (gesture, structure, anatomy, form, rhythm, accuracy)
- never be random or repetitive
- never rely on arbitrary numbers ("10 drawings in 10 minutes") unless meaningful
- always include a clear learning purpose

Each drill must follow these rules:

==============================================================
🎯 **DRILL REQUIREMENTS (STRICT)**
==============================================================

1. **ONE sentence per drill.**
2. **Must include a measurable output**  
   (number of drawings *only when useful*, or number of angles, or number of studies).
3. **Must include a specific learning focus**, such as:
   - gesture of the part
   - structural block-in
   - anatomy breakdown
   - functional movement
   - proportion accuracy
   - planar simplification
   - value organization
   - weight & tension
4. **Must include HOW the student works**, such as:
   - gesture → structure → refinement workflow
   - studying from 3 viewpoints
   - breaking into forms (boxes, cylinders, wedges)
   - copying master drawings
   - tracing anatomical landmarks
5. **Drills MUST vary.**
   You MUST mix:
   - quick gestures  
   - slow structural studies  
   - anatomy breakdown  
   - accuracy training  
   - perspective/rotation studies  
   - one advanced or analytical assignment
6. **NO drill may sound random.**
   Every drill must be meaningful and a real exercise.

==============================================================
💡 **EXAMPLES OF THE STYLE (don’t copy them)**
==============================================================

- “Do 5 quick gesture studies of the foot focusing ONLY on the compression and spread of the toes when weight is applied.”
- “Break down the toes into simple wedge forms in 3 views, emphasizing the alignment of joints.”
- “Do an anatomy overlay for 3 different toe shapes, labeling tendons and phalanges.”
- “Draw 4 rotating views of the foot to study how toe perspective changes with angle.”
- “Copy 2 foot studies from a master artist, focusing on rhythm and curvature of the toes.”

==============================================================
🧠 **TEACHER INTENT**
==============================================================

These drills should:
- build real mastery
- be highly educational
- push the student toward intermediate/advanced skill
- diagnose what beginners typically misunderstand
- correct that misunderstanding through practice

==============================================================
📌 OUTPUT FORMAT
==============================================================

Output ONLY:
- 4 to 6 bullet lines
- each starting with "- "
- no intro text
- no explanation
- no extra formatting
"""

    user_prompt = f"""
TASK:
Title: {task.title}
Description: {task.description}

Generate 5–7 professional-level practice drills.
Remember: bullet lines only.
"""

    resp = client.chat.completions.create(
        model=OPENAI_MODEL,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        temperature=0.6,
    )

    return resp.choices[0].message.content.strip()
