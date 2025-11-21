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

Prototype 2 focuses on improving usability, searchability, and content management.
These additions build directly on Prototype 1 and reflect natural user needs.

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



