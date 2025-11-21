# ✅ **SPECIFICATION.md — Final Prototype #1**

### *ArtGrow – PKMS + Task Manager + AI Assistant*

---

## **1. Overview**

ArtGrow is a **terminal-based Personal Knowledge Management System (PKMS)** designed specifically for **artists who want to grow consistently**, store drawing knowledge, manage study tasks, and receive AI-powered feedback or practice plans.

This software integrates:

1. **PKMS (Notes System)**
2. **Task Management System**
3. **Chat-style CLI interface**
4. **AI Agents (using OpenAI)**
5. **JSON-based storage**
6. **Portable Python package (Windows, macOS, Linux)**

This specification describes the **blueprint** of the system — not code, not tests — but the **intended behavior, structure, and features** of the final version.

---

## **2. Goals of the System**

* Help artists keep notes about anatomy, gesture, shading, composition, etc.
* Allow creating categorized tasks like “gesture practice,” “finish composition study,” etc.
* Provide searchability for both notes and tasks.
* Act as a personal study assistant with AI-generated:

  * note summaries
  * practice routines
* Run entirely in a terminal interface
* Store data locally in human-readable JSON

---

## **3. System Architecture**

The project is organized into the following Python modules:

### **1️⃣ final/models.py**

Defines core data structures:

* `Note`
* `Task`

Each is a dataclass with methods:

* `create(...)`
* `to_dict()`
* `from_dict(...)`

### **2️⃣ final/storage.py**

Handles all persistent JSON storage:

* `notes.json`
* `tasks.json`
* directory creation
* reading/writing JSON
* generating next IDs

### **3️⃣ final/pkms.py**

Implements the **Note** (PKMS) features:

* add-note
* list-notes
* view-note
* search-notes

### **4️⃣ final/task_manager.py**

Implements the **Task System**:

* add-task
* list-tasks
* complete-task
* delete-task
* search-tasks

### **5️⃣ final/ai_agents.py**

Implements two AI helpers:

* Summarize a note into an **art improvement tip**
* Suggest **daily practice routines** based on user struggles + notes + tasks

### **6️⃣ final/main.py**

Implements a **chat-style CLI** with a command loop:

* interprets commands
* routes to correct modules
* prints output

---

## **4. Data Model Specification**

### **Note Model**

| Field      | Type      | Description                                 |
| ---------- | --------- | ------------------------------------------- |
| id         | int       | unique ID                                   |
| title      | str       | short note title                            |
| content    | str       | full text                                   |
| tags       | list[str] | art-specific tags like “anatomy”, “gesture” |
| created_at | str       | ISO timestamp                               |
| updated_at | str       | ISO timestamp                               |

### **Task Model**

| Field        | Type | Description                    |
| ------------ | ---- | ------------------------------ |
| id           | int  | unique ID                      |
| title        | str  | short task name                |
| description  | str  | details of the task            |
| priority     | str  | low / medium / high            |
| status       | str  | todo / in-progress / done      |
| category     | str? | e.g., gesture, projects, study |
| due_date     | str? | optional                       |
| created_at   | str  | ISO timestamp                  |
| completed_at | str? | timestamp when done            |

---

## **5. Core Features**

### **A. Notes (PKMS)**

* Create notes with:

  * title
  * multiline content
  * comma-separated tags
* View individual notes
* List all notes
* Search by:

  * title
  * content
  * tags
* Notes are stored in `notes.json`

---

### **B. Task Manager**

* Create tasks with:

  * title
  * description
  * priority
  * category (optional)
  * due date (optional)
* List tasks with optional filtering (todo/done/in-progress)
* Mark tasks done
* Delete tasks
* Search tasks
* Tasks stored in `tasks.json`

---

### **C. AI Agents**

#### **1. ai-summarize-note <id>**

→ Summarizes a note as an **actionable art tip**
e.g., “Simplify the ribcage into two ellipses…”

#### **2. ai-suggest-practice**

→ Generates a **personalized practice routine**
based on:

* user's struggles
* recent notes
* recent tasks

---

### **D. CLI Interface**

Runs in terminal using:

```
python -m final.main
```

Command examples:

```
add-note
list-notes
view-note 2
search-notes gesture
add-task
list-tasks todo
complete-task 3
delete-task 3
ai-summarize-note 1
ai-suggest-practice
help
exit
```

---

## **6. Storage Specifications**

All storage uses **plain JSON**, human-readable.

Example notes.json:

```json
{
  "notes": [
    {
      "id": 1,
      "title": "Shoulder Anatomy",
      "content": "...",
      "tags": ["anatomy", "gesture"],
      "created_at": "...",
      "updated_at": "..."
    }
  ]
}
```

---

## **7. Constraints & Requirements**

* Must run with Python 3.9+
* Must run on Windows, macOS, and Linux
* No external database (JSON only)
* No GUI (terminal only)
* Code must be modular and readable
* AI features must check API key

---

## **8. Out-of-Scope (for Prototype #1)**

These **are not included yet** but could be future commits:

❌ folder/subfolder structure
❌ multimedia embedding
❌ syncing across devices
❌ GUI
❌ cloud storage

Those are possible improvements for **Prototype #2**.

Here are the **complete, clean, professor-ready features** of **Final Prototype #1** of your project *ArtGrow – PKMS + Task Manager + AI Assistant*.

This list is **exactly what you should put in SPECIFICATION.md (Prototype #1 section), DOCUMENTATION.md introduction, and SUMMARY.md**.

---

# ✅ **PROTOTYPE #1 — Feature List**

Your Prototype #1 includes **all required components** of the assignment to make it easier to understand how things evolved over time:

---

# **1. Personal Knowledge Management System (PKMS)**

A full note-taking system designed for artists.

### ✔ Add notes

* Title
* Multi-line content
* Tags (comma-separated)
* Auto timestamps (created/updated)

### ✔ List notes

* Shows ID, title, tags, updated time

### ✔ View notes

* Displays full content nicely formatted

### ✔ Search notes

Matches:

* title
* content
* tags

### ✔ JSON storage

All notes saved in:

```
final/data/notes.json
```

---

# **2. Task Management System**

Supports workflow and practice planning for artists.

### ✔ Add tasks

Fields:

* title
* description
* priority (low/medium/high)
* category (gesture, anatomy, etc.)
* due date (optional)

### ✔ List tasks

* Sorted
* Optional filter:

  * todo
  * done
  * in-progress

### ✔ Complete tasks

Marks task as “done” + timestamp

### ✔ Delete tasks

### ✔ Search tasks

Matches:

* title
* description
* category

### ✔ JSON storage

```
final/data/tasks.json
```

---

# **3. Terminal-Based Chat Interface**

Runs as:

```
python -m final.main
```

### ✔ Command loop

Continuously reads user commands and executes functions.

### ✔ Helpful UI

* Banner
* Help menu
* Human-readable outputs
* Error messages
* No crashes on bad input

### ✔ All commands available

```
add-note
list-notes
view-note <id>
search-notes <query>
add-task
list-tasks [status]
complete-task <id>
delete-task <id>
search-tasks <query>
ai-summarize-note <id>
ai-suggest-practice
help
exit
```

This satisfies the **chat interface** requirement of the course.

---

# **4. AI Agents (OpenAI-based)**

(Mandatory for CSC299 final)

### ✔ AI Note Summarization

```
ai-summarize-note <id>
```

Turns a full note into a **short, actionable art tip**.

### ✔ AI Practice Routine

```
ai-suggest-practice
```

Generates a study plan using:

* user struggles
* recent notes
* recent tasks

### ✔ Proper error handling

If OPENAI_API_KEY is missing, displays a clean message.

---

# **5. JSON-Based Storage Architecture**

Fully meets requirements:

* no database
* no external server
* simple, portable data files
* automatically creates folder
* loads safely even if file empty

---

# **6. Modular Code Architecture**

All files properly separated:

* `main.py` → CLI
* `pkms.py` → Notes logic
* `task_manager.py` → Task logic
* `ai_agents.py` → AI functions
* `storage.py` → file handling
* `models.py` → dataclasses
* `config.py` → API key reading

You have **excellent modularity**, which teachers LOVE.

---

# **7. Robust Error Handling**

Prototype 1 already handles:

* missing note/task
* invalid IDs
* empty queries
* corrupted JSON
* missing API key
* blank input
* incorrect command syntax

---

# **8. Documentation & Structure**

You now have:

* SPECIFICATION.md
* TESTS.md
* DOCUMENTATION.md

All at root.
These are core grading elements.

---

# **9. Fully Working End-to-End System**

You can:

1. Add a note
2. Add a task
3. Search them
4. View them
5. Get AI suggestions
6. Manage everything through a chat interface
7. Store data
8. Retrieve data

---

Perfect — these are **excellent**, clean, realistic Prototype 2 features.
Your list is exactly the kind of incremental improvement your professor expects.
Now I’ll turn your raw list into **clean, professor-ready SPECIFICATION.md sections** for:

* **Prototype 2 — Planned Improvements**
* **Prototype 3 — Stretch Ideas**

I will also fix the order, combine similar items, and make it coherent.

---

# ## **Prototype 2 — Planned Improvements**

Prototype 2 focuses on improving usability, searchability, and content management. These additions build directly on Prototype 1 and reflect natural user needs.

### **1. Edit Notes**

Add a command:

```
edit-note <id>
```

Users will be able to modify:

* title
* content
* tags

Changes update the `updated_at` timestamp automatically.

---

### **2. Edit Tasks**

Add a command:

```
edit-task <id>
```

Editable fields:

* title
* description
* priority
* category
* due date

This significantly improves the task workflow for artists refining study plans.

---

### **3. Improved Search Engine**

Enhance searching for both notes and tasks:

* support **partial matches** (already partly works but we refine it)
* support **multiple keywords**
* allow results sorted by relevance (optional stretch)

Example queries:

```
search-notes anatomy gesture
search-tasks shading hands
```

This makes the system feel more “Notion-like.”

---

### **4. Add “in-progress” Status**

Currently status options are:

```
todo
done
```

Prototype 2 adds:

```
in-progress
```

New commands:

```
start-task <id>
in-progress tasks visible in list-tasks
```

This supports better workflow modeling.

---

### **5. Tag-Based Note Filtering**

Add a command:

```
filter-notes tag anatomy
filter-notes tag gesture
```

Allows artists to group study notes by topic.

---

### **6. Delete Notes (with confirmation)**

Prototype 1 intentionally does NOT allow deleting notes.

Prototype 2 adds:

```
delete-note <id>
```

With safety confirmation:

```
Are you sure? (y/n)
```

---

### **7. Command History / Logging**

Add a simple log file:

```
logs/commands.log
```

Record:

* timestamp
* executed command
* optional arguments

Purpose:

* debugging
* user awareness
* meets “AI agent / PKMS evolution” documentation

---

### **8. Automatic Timestamps Everywhere**

Prototype 1 already adds timestamps for creation and updates.

Prototype 2 adds automatic timestamps to:

* task status changes
* task edits
* note edits
* logs

This helps artists track progress.

---

### **9. Lightweight Encryption (Optional for P2 but doable)**

Encrypt note content using simple AES + password.

Goal:

* protect sensitive study notes or personal thoughts
* keep it simple enough for terminal use

Encryption is **local only**, no cloud sync.

---
Here is a **clean, professor-ready Prototype 2 section** that you can paste directly into your **SPECIFICATION.md** underneath Prototype 1.

It is formatted exactly the way a real software specification should be written — structured, clear, technical, and ready for grading.

---

# ✅ **Prototype 2 — Specification (Planned & Implemented Improvements)**

Prototype 2 builds directly on Prototype 1 with the goal of making ArtGrow more usable, more flexible, and more aligned with the workflow of real artists. This prototype adds **editing**, **better searching**, **status improvements**, **tag filtering**, **note deletion**, **logging**, and **automatic timestamps**.

These upgrades refine the original PKMS + Task Manager and prepare the system for future prototypes.

---

## **1. Goals of Prototype 2**

Prototype 2 focuses on:

* Improving **content correction and editing** abilities
* Enhancing **search and filtering**
* Increasing workflow quality with **in-progress status**
* Adding **safe deletion** for notes
* Improving system transparency with **logging**
* Ensuring data remains consistent with **auto timestamps**

This prototype does NOT add new AI features; it improves the core PKMS + Task Manager experience.

---

# **2. New Features Added in Prototype 2**

---

## **2.1 Edit Notes**

### **Command:**

```
edit-note <id>
```

### **Description:**

Allows the user to modify an existing note’s:

* title
* content
* tags

When editing is complete, the system automatically updates:

* `updated_at` timestamp

### **Purpose:**

Users often make mistakes or want to refine notes. Editing improves long-term usability and accuracy of the PKMS.

---

## **2.2 Edit Tasks**

### **Command:**

```
edit-task <id>
```

### **Editable Fields:**

* title
* description
* priority (low/medium/high)
* category
* due date

### **Purpose:**

Tasks evolve as the artist refines their study plan. Editing allows dynamic updates instead of deleting/recreating tasks.

---

## **2.3 Improved Search Engine (Multi-Keyword Search)**

### **Commands:**

```
search-notes <keywords>
search-tasks <keywords>
```

### **Behavior:**

* Supports **multiple keywords**
* Supports **partial matches**
* Returns entries that match ANY keyword
* Makes searching more powerful and flexible

### **Purpose:**

Artists often need to search multiple related topics at once. This creates a “Notion-like” experience in a terminal.

---

## **2.4 Add “in-progress” Task Status**

### **Command:**

```
start-task <id>
```

### **Behavior:**

* Changes status from `todo` → `in-progress`
* Automatically updates `updated_at`
* Visible inside:

```
list-tasks in-progress
```

### **Purpose:**

Represents real workflow:

✔ todo → in-progress → done

Makes the task system more realistic and practical.

---

## **2.5 Tag-Based Note Filtering**

### **Command:**

```
filter-notes tag <tagname>
```

### **Behavior:**

* Filters notes by tag
* Useful for grouping by subject (e.g., anatomy, perspective, gesture)

### **Purpose:**

Artists often study by topic. Tag filtering helps them locate related notes instantly.

---

## **2.6 Delete Notes (with Safety Confirmation)**

### **Command:**

```
delete-note <id>
```

### **Workflow:**

System asks:

```
Are you sure you want to delete this note? (y/n)
```

Deletion only occurs on confirmation.

### **Purpose:**

Prevents accidental loss while giving control over note cleanup.

---

## **2.7 Command History Logging**

### **Log file created:**

```
final/logs/commands.log
```

### **Each entry tracks:**

* timestamp
* command used
* arguments

### **Purpose:**

* Helps user understand usage patterns
* Supports debugging
* Shows PKMS evolution over time

---

## **2.8 Automatic Timestamps Everywhere**

Prototype 2 expands timestamp usage so that the system tracks:

* note edits
* task edits
* status changes
* deletions
* command history events

### **Purpose:**

This gives the user clearer visibility into their progress and makes the system feel more professional and reliable.

---

# **3. Summary of Architecture Changes in Prototype 2**

| Component           | Description                                                                 |
| ------------------- | --------------------------------------------------------------------------- |
| **pkms.py**         | Added edit-note, delete-note, tag filter, and timestamp updates             |
| **task_manager.py** | Added edit-task, start-task, multi-keyword search, improved status handling |
| **storage.py**      | Added command logging system                                                |
| **models.py**       | Added `updated_at` to Task model and edit timestamp logic                   |
| **main.py**         | Added routing for all new commands in the CLI                               |

---

# **4. Out-of-Scope Features (Future Prototypes)**

These are NOT included in Prototype 2:

❌ encryption
❌ nested folders
❌ multi-user sync
❌ GUI
❌ Notion-style linking
❌ complex AI agents

These remain possibilities for Prototype 3 or 4.

---

# **5. Status of Prototype 2**

### Prototype 2 is **complete**, delivering:

✔ editing
✔ improved search
✔ status upgrades
✔ tag filtering
✔ deletion
✔ logging
✔ timestamps

This spec documents expected behavior for everything implemented.

```

# ✅ **Prototype 3 — Planned AI Enhancements**

Prototype 3 focuses entirely on improving the intelligence and automation of the system.
These features extend the AI agent capabilities added in Prototype 1 and 2.

### **1. AI Task Auto-Analysis**

A command that analyzes all tasks and gives:

* which ones are critical
* which ones are overdue
* which ones the user should focus on today.

### **2. AI Generate Tasks From a Note**

Create tasks automatically based on the content of a selected note.
Example:

```
ai-generate-tasks 2
```

### **3. AI Skill Gap Analysis**

Given user struggles, notes, and tasks, the AI identifies:

* weak areas
* missing topics
* suggested learning priorities

### **4. Smart Chat Mode for Artists**

A conversational assistant:

```
art-chat
```

Behaves like a drawing mentor:

* answers art questions
* references stored notes/tasks
* gives exercise suggestions

### **5. AI Auto-Tag Notes**

AI reads a note and automatically assigns tags.
Useful for long notes or beginners who don’t know tagging conventions.

### **6. AI Summaries for All Notes**

A bulk summarizer:

```
ai-summary-all
```

Creates short summaries for every note to help users review quickly.

### **7. Practice Routine 2.0**

More advanced version of the existing practice routine:

* time-based
* difficulty-based
* skill-focused
* uses note content + task history

### **8. Improve-Note Command**

AI rewrites or enhances a selected note to make:

* structure clearer
* explanations stronger
* learning points more explicit

Command:

```
ai-improve-note <id>
```

### **9. Portfolio Feedback Mode**

User provides a description of an artwork:

```
portfolio-feedback
```

AI gives:

* strengths
* weaknesses
* composition notes
* gesture/structure advice

---

