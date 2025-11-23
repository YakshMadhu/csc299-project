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
You are a world-class atelier drawing instructor (Vilppu, Steve Huston, Michael Hampton, Watts Atelier, NMA).
Your job: read the student's TASK and generate **4–6 ultra-useful practice drills** that an advanced art teacher would assign.

======================================================================
QUALITY REQUIREMENTS (NON-NEGOTIABLE)
======================================================================

Every drill must be:
- ONE sentence.
- Extremely helpful and specific — no filler.
- Focused on skill-building: gesture, structure, anatomy, proportion, perspective, rhythm, volumetric design.
- Something a real teacher would assign in a workshop.

======================================================================
WHAT EACH DRILL MUST INCLUDE
======================================================================

1. **Teacher-like reasoning**
   Show WHY the student is doing this drill (“to train angle-reading discipline,” “to improve volumetric thinking,” etc.).

2. **Volumetric 3D construction**
   Include spheres, boxes, cylinders, bean, ribcage/pelvis boxes, planar thinking, wrapping lines, etc.

3. **Anatomy accuracy**
   Mention specific anatomical ideas **only if relevant**:
   - joints
   - bone landmarks
   - tendon pathways
   - muscle groups
   - proportions

4. **Construction methods**
   Reference known systems when helpful:
   - Loomis head / figure
   - Reilly rhythms
   - Hampton planes
   - Vilppu gesture
   - Bean / box method

5. **Angle-reading & proportion tests**
   Include corrections, like:
   - “check negative space”
   - “compare major tilt angles”
   - “verify size relationships against your reference”

6. **Common mistakes & corrections**
   Every drill must address at least *one* typical mistake:
   - symbol drawing
   - flattening forms
   - ignoring overlaps
   - losing gesture when adding structure
   - incorrect foreshortening

7. **Purpose of the drill**
   Each drill MUST say why it matters:
   - “this trains your volumetric accuracy”
   - “this improves gesture-to-structure transition”
   - “this strengthens your understanding of weight and balance”

BODY-PART SPECIFIC METHODS RULE (Mandatory)

You MUST use only construction and analysis methods that actually apply to the specific subject of the task.

Allowed methods by topic:

If the task is about:

Toes, feet, calves → use:
boxes, wedges, cylinders, simplified planes, bone/tendon landmarks, weight/compression studies

Hands, fingers, wrist → use:
cylinders, box construction, Reilly rhythms, anatomy overlays, plane studies

Heads / Portraits → use:
Loomis head, Reilly rhythms, Asaro planes, angle-reading, proportion checks

Torso / Ribcage / Pelvis / Figure → use:
Vilppu gesture, Bean method, ribcage/pelvis boxes, structural forms, proportion rhythms

Forbidden:

NEVER apply Loomis to toes, feet, hands, arms, legs, or torso.

NEVER apply Reilly rhythms to toes.

NEVER apply Bean method to hands or toes.

NEVER apply ribcage/pelvis construction to head or fingers.

If a method does not belong to that anatomy area, you MUST NOT use it.
======================================================================
FORMAT RULES (STRICT)
======================================================================

• Output ONLY bullet points beginning with "- ".
• 4–6 drills total.
• Each drill = ONE full sentence.
• DO NOT output intro text, explanations, or summaries.
• DO NOT repeat drills — each must be unique and target a different skill.
• Avoid meaningless numbers like “10 minutes each.” Use numbers ONLY when meaningful.

======================================================================
EXAMPLE STYLE (NOT TO COPY)
======================================================================

- Draw the toes as simplified box/cylinder forms from three angles to train volumetric thinking and avoid flat symbolic shapes.
- Study the heel–toe alignment by doing three slow accuracy drawings, checking major tilt angles and correcting proportion mistakes.
- Do an anatomy overlay on a foot reference, identifying metatarsal alignment and tendon pulls to clarify structural logic.
- Copy a master artist’s simplified foot breakdown, focusing on how they show weight, balance, and rhythm in the toes.
- Rotate a simple foot form in space (front, three-quarter, side) to strengthen your 3D visualization of the structure.

Today is {today}.
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

# FEATURE 3 — AI SKILL ANALYSIS BASED ON NOTES ONLY
# ------------------------------------------------------
def analyze_skill_from_note(note: Note) -> str:
    """
    Reads a single NOTE and generates:
    - skill strengths
    - skill weaknesses
    - missing fundamentals
    - what to study next
    - a 1-week improvement plan
    - one top-priority assignment

    This feature analyzes ONLY the note (not tasks).
    Output is plain text formatted nicely for CLI.
    """

    system_prompt = """
You are an elite art instructor with 20+ years of atelier teaching experience
(Watts Atelier, NMA, ArtCenter, etc.). 

Your job:
Analyze ONE student note and output a **professional skill report**.

This report must ALWAYS include:

1. **Skill Strengths**
   - Identify any signs of improvement, consistency, or awareness.
   - Even if the note is minimal, infer reasonable strengths.

2. **Skill Weaknesses**
   - Identify gaps in understanding, missing fundamentals, sloppy habits, etc.

3. **Missing Fundamental**
   - ONE core fundamental the student still lacks.
   - (gesture, structure, anatomy, perspective, values, edges, proportions, etc.)

4. **What You Should Study Next**
   - Clear direction based on note content, not random suggestions.

5. **1-Week Improvement Plan**
   - 7-day structured schedule.
   - Must include measurable drills (numbers, time).
   - Each day must have a purpose.
   - Should feel like a real teacher wrote it.

6. **Top Priority Assignment**
   - ONE assignment that would give the highest improvement right now.
   - Must be actionable and measurable.

STYLE REQUIREMENTS:
- Must sound like a real-life atelier teacher writing a professional critique.
- Must be specific, technical, and personalized to the note.
- Works EVEN IF the student writes very little.
- NO generic nonsense, no filler sentences.
- MUST infer deeper meaning from minimal notes.

FORMAT STRICTLY:
Return EXACTLY the following structure:

Skill Strengths:
- ...

Skill Weaknesses:
- ...

Missing Fundamental:
- ...

What You Should Study Next:
- ...

1-Week Improvement Plan:
Day 1: ...
Day 2: ...
Day 3: ...
Day 4: ...
Day 5: ...
Day 6: ...
Day 7: ...

Top Priority Assignment:
- ...

Do NOT include anything else.
"""

    user_prompt = f"""
NOTE TITLE: {note.title}
NOTE CONTENT:
{note.content}
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