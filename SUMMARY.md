# **SUMMARY.md – Development Process for ArtGrow**

ArtGrow began as a simple idea: I wanted a system that supported the way artists actually think and work. Artists constantly switch between learning theory (anatomy, gesture, perspective) and doing practice routines (assignments, drills, studies). Because of that, my very first brainstorming session produced a clear separation:
**PKMS = The mind** (theory, notes, class material, anatomy breakdowns)
**Tasks = The hands** (practice routines, studies, projects)

This distinction guided the entire project from the prototype to the final version. As the software evolved, I realized that building a system for artists required the same structure artists themselves use: learn → practice → refine → repeat. Ironically, the development of the software mirrored the exact learning cycle it was built to support.

---

## **Prototype 1 — Brainstorming, First Steps, and Core Structure**

My initial goal was simply to prove that I could build a functional terminal-based PKMS. Prototype 1 only had three commands: add a note, list notes, and view a note. JSON storage was minimal, and the CLI loop was basic.

During this phase, I used **ChatGPT as a conversational assistant**. I asked questions like:

* “Should notes have timestamps?”
* “How should I structure the modules?”
* “What’s the simplest way to store data?”

This was also the first time I learned something important about myself as a developer: I often try to jump too quickly into adding features without a plan. Writing a planning document (the first draft of `specification.md`) forced me to slow down and outline the essentials. This prevented scope creep and gave me a roadmap.

I realized early on that planning is a skill—and that I was learning how to plan *as I built the project*.

---

## **Prototype 2 — Editing, Searching, Tagging, and Cleaner Architecture**

Prototype 2 was where the project became a real system rather than a simple script. I reorganized the entire codebase into modular files (`main.py`, `pkms.py`, `task_manager.py`, `storage.py`), which taught me the importance of clear boundaries between responsibilities.

This phase introduced:

* editable notes
* editable tasks
* search
* tag filtering
* safe deletion
* command logging
* improved error handling

I used **ChatGPT extensively for architectural guidance**, especially when deciding how to structure `main.py` so all commands followed the same pattern:

1. validate input
2. convert IDs
3. call the appropriate function
4. show friendly results

This led to a complete rewrite of the CLI handler. The original version was a messy chain of `if-elif` statements with repeated logic. ChatGPT helped me refactor it into a more predictable structure.

GitHub Copilot became useful in this phase too—particularly for writing repetitive patterns like `try/except`, updating JSON files, or generating placeholder functions. However, I learned that Copilot sometimes generates incorrect assumptions or outdated code, so I leaned more heavily on ChatGPT for reasoning and Copilot only for small snippets.

The creation of `tests.md` and manual tests helped me understand edge cases better. I discovered corrupted JSON, empty input crashes, invalid ID errors, and missing fields—all issues that only surfaced once I treated the system like real software.

This phase taught me discipline: returning to my code with the intention to refine it, not just patch it.

---

## **Prototype 3 — AI Modules, Major Refactor, and Real Growth**

Prototype 3 transformed ArtGrow from a PKMS into a multi-agent AI ecosystem. I added:

* **AI Summarizer**
* **AI Practice Generator**
* **AI Skill Analysis**
* **AI Mentor**
* **AI Art Critique Engine**
* **AI Anatomy Expert**

Integrating AI required a fresh refactor because the system now needed consistent access to notes, tasks, IDs, and data validation. I used ChatGPT heavily for:

* designing strict, structured AI prompts
* ensuring stable JSON outputs
* improving error messages
* refining the text formatting for terminal display
* generating content for video demonstrations
* debugging malformed or failing API calls

A major false start happened when I tried to build **one universal AI function**. It was unpredictable and would often return inconsistent formats. ChatGPT advised me to split the system into **multiple specialized AI agents**, each with its own prompt and expectations. This fixed the reliability problems instantly.

I also experimented with adding a `view-task-description` command, but after multiple design attempts, I realized it wasn’t necessary for Prototype 3. I learned something important: not every idea must be implemented immediately. Good software development requires saying **no** to features sometimes.

This phase also taught me how to think about user experience—how the CLI should behave, how messages should be formatted, and how to create a smooth workflow.

---

## **What I Learned About Myself as a Developer**

* I work best when I break problems into prototypes.
* Planning documents make me more organized.
* I tend to overbuild early, and refactoring helps me regain clarity.
* AI is extremely powerful for guiding thought, but final decisions must always be mine.
* I learned to value readability and user experience as highly as raw functionality.
* I discovered the importance of thinking like a user, not just a programmer.

---

## **Conclusion**

ArtGrow grew from a tiny note-taking script into a structured PKMS + Task Manager + multi-agent AI system. This project taught me how to plan, iterate, test, and refine software using modern tools like ChatGPT and Copilot. More importantly, it taught me how *I* think as a developer—how I design, how I troubleshoot, how I evolve ideas, and how I bring a system from imagination to a polished final product.

---
