# ✅ **DOCUMENTATION.md — User Guide**

### *ArtGrow – PKMS + Task Manager + AI Assistant (CLI Edition)*

---

# **1. Introduction**

ArtGrow is a command-line tool designed for artists who want to:

* Store structured drawing notes
* Organize art practice tasks
* Search knowledge efficiently
* Receive personalized AI study guidance
* Maintain consistent growth in drawing

This document explains **how to use** the system — from installation to running commands.

---

# **2. Installation & Setup**

### **Step 1 — Install required package**

Open a terminal and run:

```
pip install openai
```

### **Step 2 — Navigate to the project**

From the root of your `csc299-project` repository:

```
cd csc299-project
```

### **Step 3 — Set your API key (optional but required for AI features)**

#### macOS/Linux:

```
export OPENAI_API_KEY="sk-yourkey"
```

#### Windows PowerShell:

```
$env:OPENAI_API_KEY="sk-yourkey"
```

AI features will **not** work without a key,
but all PKMS/Task Manager commands work normally.

---

# **3. Running the Application**

From the root directory:

```
python -m final.main
```

If everything is set up correctly, you will see the banner:

```
========================================
   ArtGrow – PKMS & Task Coach (CLI)
========================================
Type 'help' to see commands.
```

---

# **4. Command Overview**

ArtGrow uses a **chat-style interface**.

Type commands into the terminal.
Press **Enter** after each.

To see all commands at any time:

```
help
```

---

# **5. Notes (PKMS) System**

Notes allow artists to store structured learning content such as:

* anatomy information
* gesture principles
* perspective rules
* shading techniques

### **5.1 Create a Note**

```
add-note
```

You will be prompted:

```
Title:
Content:  (finish with an empty line)
Tags: anatomy, gesture, shading
```

Notes are saved automatically.

---

### **5.2 List All Notes**

```
list-notes
```

Shows note ID, title, tags, and update time.

---

### **5.3 View One Note**

```
view-note <id>
```

Example:

```
view-note 3
```

Displays full content, tags, timestamps.

---

### **5.4 Search Notes**

```
search-notes <query>
```

Example:

```
search-notes gesture
```

Matches against:

* title
* content
* tags

---

# **6. Task Manager**

Tasks are used to track:

* drawing practice
* long-term art projects
* study routines
* deadlines

---

### **6.1 Add a Task**

```
add-task
```

You will be asked for:

* title
* description
* priority (`low/medium/high`)
* category (`gesture, anatomy, project…`)
* due date (`YYYY-MM-DD`)

---

### **6.2 List Tasks**

```
list-tasks
```

Or filter:

```
list-tasks todo
list-tasks done
list-tasks in-progress
```

---

### **6.3 Mark a Task as Done**

```
complete-task <id>
```

Example:

```
complete-task 1
```

---

### **6.4 Delete a Task**

```
delete-task <id>
```

---

### **6.5 Search Tasks**

```
search-tasks <query>
```

Example:

```
search-tasks anatomy
```

Matches title, description, and category.

---

# **7. AI Features (Optional)**

ArtGrow includes **two AI assistants**, built for artists.

AI works only if `OPENAI_API_KEY` is set.

---

## **7.1 Summarize a Note into an Art Tip**

```
ai-summarize-note <id>
```

Example:

```
ai-summarize-note 2
```

Output example:

```
AI Tip:
--------
Focus on simplifying the torso using basic shapes...
--------
```

---

## **7.2 Suggest a Personalized Practice Routine**

```
ai-suggest-practice
```

You will enter your struggles:

```
I struggle with drawing heads.
My shading looks flat.
```

AI outputs a routine like:

```
1. 10 minutes of gesture warmup
2. Practice the Loomis head for 20 minutes
3. 5 shading drills focusing on edge control
```

---

# **8. Storage Location**

All your data is saved in:

```
final/data/notes.json
final/data/tasks.json
```

Files are:

* Human-readable
* Easy to modify manually
* Simple to back up

---

# **9. Common Problems & Solutions**

### **Problem: "OPENAI_API_KEY is not set"**

AI features cannot run.
Set your key using environment variables.

---

### **Problem: JSON file corrupted**

Delete the `.json` file.
The system will recreate a fresh one.

---

### **Problem: Command not recognized**

Check your spacing:

❌ `view note 1`
✔ `view-note 1`

---

### **Problem: Code crashes when adding a note**

Ensure you finish content entry with **an empty line**.

---

# **10. Closing the Program**

Type:

```
exit
```

or:

```
quit
```

---

# **11. Summary for Users**

ArtGrow is built to be:

* intuitive
* simple
* flexible
* helpful for long-term art improvement

If you keep adding notes and tasks consistently,
The AI assistant will give you increasingly personalized routines.

---
Here is your **professor-ready Prototype 2 section for `DOCUMENTATION.md`**.
This is written exactly like a real software user manual — simple, clear, and focused ONLY on *how to use* the system.

You can **copy–paste this directly** into your `DOCUMENTATION.md` under the heading for Prototype 2.

---

## **Prototype 2 — User Guide & Instructions**

Prototype 2 builds on the original version of ArtGrow by adding powerful editing tools, richer searching, task workflow improvements, safe deletion, tagging, and full command logging. This document explains **HOW to use the system**, including examples.

---

# ⭐ 1. How to Run the Program

Make sure you are in the **root folder** of your `csc299-project` repository:

```
cd csc299-project
```

Run the application:

```
python -m final.main
```

You should see:

```
========================================
   ArtGrow – PKMS & Task Coach (CLI)
========================================
Type 'help' to see commands.
```

---

# ⭐ 2. Commands Overview

Below is the **full list of commands** available in Prototype 2.

---

# 📘 **Notes (PKMS) Commands**

### **Create a note**

```
add-note
```

Multi-line content is supported. Finish by pressing **Enter on an empty line**.

---

### **List all notes**

```
list-notes
```

---

### **View a note**

```
view-note <id>
```

Example:

```
view-note 2
```

---

### **Search notes**

```
search-notes <keywords>
```

Supports **multiple keywords**:

```
search-notes anatomy gesture shading
```

---

### **Filter notes by tag**

```
filter-notes tag <tagname>
```

Example:

```
filter-notes tag anatomy
```

---

### **Edit an existing note**

```
edit-note <id>
```

You may edit the:

* title
* content
* tags

Example:

```
edit-note 1
```

---

### **Delete a note (with confirmation)**

```
delete-note <id>
```

System will ask:

```
Are you sure? (y/n)
```

---

# 🗂 **Task Manager Commands**

### **Add a task**

```
add-task
```

You will enter:

* title
* description
* priority
* category
* due date (optional)

---

### **List tasks**

```
list-tasks
list-tasks todo
list-tasks done
list-tasks in-progress
```

---

### **Search tasks**

```
search-tasks <keywords>
```

Supports multiple keywords:

```
search-tasks shading hands anatomy
```

---

### **Mark a task as in-progress**

```
start-task <id>
```

Example:

```
start-task 3
```

---

### **Mark a task as done**

```
complete-task <id>
```

---

### **Edit a task**

```
edit-task <id>
```

You may edit:

* title
* description
* priority
* category
* due date

Example:

```
edit-task 4
```

---

### **Delete a task**

```
delete-task <id>
```

---

# 🤖 **AI Agent Commands**

### **Summarize a note**

```
ai-summarize-note <id>
```

Provides a short **art improvement tip**.

---

### **Get a practice routine**

```
ai-suggest-practice
```

Describe your struggles (multiline). Press Enter on an empty line to finish.

---

# 🧾 **Command Logging**

Every command you type is logged automatically in:

```
final/logs/commands.log
```

Each log entry has:

* timestamp
* command
* arguments

Useful for debugging and showing project evolution.

---

# 🕒 **Automatic Timestamps**

Prototype 2 automatically timestamps:

* note edits
* task edits
* task status changes
* creation times
* completion times
* logging events

You will see fields like:

```
created_at: 2025-11-20T14:33:01
updated_at: 2025-11-20T15:01:22
completed_at: 2025-11-21T09:12:10
```

---

# 🧪 **Example Session**

```
> add-note
Title: Shoulder Muscles
Content:
The deltoid has 3 heads...
<empty line>

Tags: anatomy, torso
Saved note #1

> add-task
Title: Draw ribcage
Description: Practice 10 studies
Priority: high
Category: anatomy
Due date: 2025-11-22
Saved task #1

> start-task 1
Task #1 marked as in-progress.

> edit-note 1
(change title/content/tags)

> filter-notes tag anatomy

> search-tasks draw ribcage

> delete-note 1
Are you sure? (y/n): y
```

---

# 🎯 What Prototype 2 Achieves

This version provides:

✔ Editing (notes + tasks)
✔ More powerful search
✔ Tag filtering
✔ Safe deletion
✔ Better workflow (in-progress status)
✔ Full command logging
✔ Automatic timestamp tracking
✔ Improved user experience

---

# ✅ **DOCUMENTATION.md — User Guide (Prototype 3)**

### *ArtGrow – PKMS + Task Manager + Multi-Agent AI Assistant (CLI Edition)*

**Version:** Prototype 3
**Environment:** Windows, macOS, Linux (Python 3.x)
**Data Storage:** JSON files (portable, human-readable)

---

# **1. Introduction**

ArtGrow Prototype 3 is a command-line productivity system built for artists, students, and creators who want a unified workflow combining:

* A **Personal Knowledge Management System (PKMS)**
* A **Task Manager for art study, projects, and routines**
* A **Terminal-based chat interface**
* **Five specialized AI assistant modules**:

  * AI Summarizer (notes → tips)
  * AI Practice Generator (tasks → drills)
  * AI Skill Analyst (notes → strengths/weaknesses/plan)
  * AI Mentor (ask any art question)
  * AI Art Critic (formal critique system)
  * AI Anatomy Expert (species/body-part anatomy)

Prototype 3 is more powerful, more intelligent, and more complete than the previous versions.

This guide explains **HOW to use the system**, not how it’s built.

---

# **2. Installation & Setup**

## **2.1 System Requirements**

* Python 3.9+
* Terminal access (Windows / macOS / Linux)
* Optional: OpenAI API key for AI features

---

## **2.2 Install Dependencies**

From your terminal:

```
pip install openai
```

---

## **2.3 Navigate to Your Project**

```
cd csc299-project
```

---

## **2.4 Set Your AI Key (Required for AI commands)**

### macOS / Linux:

```
export OPENAI_API_KEY="sk-yourkey"
```

### Windows PowerShell:

```
$env:OPENAI_API_KEY="sk-yourkey"
```

Without a key:

* PKMS works
* Tasks works
* AI commands will display an error

---

# **3. Running the Program**

Start ArtGrow:

```
python -m final.main
```

You should see:

```
========================================
   ArtGrow – PKMS & Task Coach (CLI)
========================================
Type 'help' to see commands.
Type 'quit' or 'exit' to leave.
```

The system is now active.

---

# **4. General Command Usage**

ArtGrow uses a **chat-style interface**.
You simply type commands like:

```
add-note
search-tasks anatomy
ai-critique A standing figure...
```

At any time:

```
help
```

Shows the complete command list.

---

# **5. Notes (PKMS) System**

Notes store theory, breakdowns, observations, anatomy rules, and anything you want to remember.

---

## **5.1 Create a Note**

```
add-note
```

The program prompts:

```
Title:
Content:   (finish with an empty line)
Tags: anatomy, gesture, shading
```

Contents can span multiple lines.
Press **Enter on an empty line** to finish.

---

## **5.2 List All Notes**

```
list-notes
```

Shows:

* ID
* Title
* Tags
* Created/updated timestamps

---

## **5.3 View a Note**

```
view-note <id>
```

Example:

```
view-note 5
```

---

## **5.4 Search Notes by Keywords**

```
search-notes <word1 word2 word3>
```

Examples:

```
search-notes gesture
search-notes shading head proportions
```

Matches:

* Title
* Content
* Tags

---

## **5.5 Filter Notes by Tag**

```
filter-notes tag <tagname>
```

Example:

```
filter-notes tag anatomy
```

---

## **5.6 Edit a Note**

```
edit-note <id>
```

You can modify:

* title
* content
* tags

---

## **5.7 Delete a Note**

(with confirmation safety)

```
delete-note <id>
```

System will ask:

```
Are you sure? (y/n)
```

---

# **6. Task Manager System**

Tasks help organize:

* art practice routines
* studies
* long-term drawing projects
* homework
* deadlines

---

## **6.1 Add a Task**

```
add-task
```

The program prompts for:

* Title
* Description
* Priority: `low/medium/high`
* Category
* Due Date (`YYYY-MM-DD`)

---

## **6.2 List Tasks**

```
list-tasks
```

Filtered:

```
list-tasks todo
list-tasks in-progress
list-tasks done
```

---

## **6.3 Mark a Task as In-Progress**

```
start-task <id>
```

---

## **6.4 Mark a Task as Done**

```
complete-task <id>
```

---

## **6.5 Search Tasks**

```
search-tasks <keywords>
```

Example:

```
search-tasks shading gesture
```

---

## **6.6 Edit an Existing Task**

```
edit-task <id>
```

You can change:

* Title
* Description
* Priority
* Category
* Due Date

---

## **6.7 Delete a Task**

```
delete-task <id>
```

---

# **7. AI Features — Prototype 3 (New & Expanded)**

Prototype 3 introduces **5 different AI agents**, each with a different purpose.

---

# ⭐ **7.1 AI Summarizer — Convert Notes into Tips**

```
ai-summarize-note <id>
```

Example:

```
ai-summarize-note 3
```

Output (example):

```
AI Tip:
--------
Focus on aligning the ribcage tilt with pelvic tilt for naturalistic poses.
--------
```

---

# ⭐ **7.2 AI Practice Generator — Turn Tasks Into Drills**

```
ai-generate-practice <id>
```

Example:

```
ai-generate-practice 1
```

Output sample:

```
Practice Drills:
1. 10 torso studies using boxes
2. 15 ribcage rotation quick sketches
3. 3 timed 5-minute poses focusing on tilt/lean
```

---

# ⭐ **7.3 AI Skill Analysis — Strengths, Weaknesses, Plan**

```
ai-skill-analysis <id>
```

You pass a note ID, and AI produces:

* Strengths
* Weaknesses
* A training roadmap

Example:

```
ai-skill-analysis 4
```

Output sample:

```
Strengths: Good understanding of perspective layering.
Weaknesses: Overuse of parallel lines in cylindrical forms.
Training Plan:
- 20 ellipse drills daily
- Practice drawing cylinders in 3-point perspective
...
```

---

# ⭐ **7.4 AI Art Mentor — Ask ANY Question**

```
ai-mentor <your question>
```

Example:

```
ai-mentor how do i improve shading transitions
```

The AI gives:

* Methods
* Drills
* Explanations
* Warnings
* Best practices

---

# ⭐ **7.5 AI Art Critique — Advanced Error Detection**

```
ai-critique <your description>
```

You write a **long, detailed, neutral** drawing description.
AI returns:

* Structural weaknesses
* Proportion issues
* Perspective drift
* Shading issues
* Missing details in your description

Example:

```
ai-critique A crouching figure with the ribcage leaning forward...
```

---

# ⭐ **7.6 AI Anatomy Expert — ANY Species + ANY Body Part**

```
ai-anatomy <species> <body_part>
```

Examples:

```
ai-anatomy human forearm
ai-anatomy eagle wing
ai-anatomy octopus tentacle
ai-anatomy horse shoulder
ai-anatomy lion paw
```

This agent returns:

* Full bone breakdown
* All muscles (origins, insertions, actions)
* Biomechanics and movement
* Functional behavior and adaptations

This is a **scientific module**, not an art module.

---

# **8. Storage System**

All data is stored in portable JSON:

```
final/data/notes.json
final/data/tasks.json
```

Properties:

* Human-readable
* Cross-platform
* Auto-updated
* Safe to manually backup

---

# **9. Command Logging (Prototype 3)**

Every action is logged in:

```
final/logs/commands.log
```

Each entry includes:

* timestamp
* command
* arguments
* session history

Useful for:

* debugging
* academic evaluation
* version tracking

---

# **10. Common Issues & Fixes**

### ❌ AI Error: "OPENAI_API_KEY not set"

Set your key again:

```
$env:OPENAI_API_KEY="sk-..."
```

### ❌ Crash when creating note

You MUST end content with an **empty line**.

### ❌ Unrecognized command

Commands use **hyphens**, not spaces:

❌ `view note 3`
✔ `view-note 3`

### ❌ JSON corrupted

Delete file:

```
rm final/data/notes.json
```

Program auto-rebuilds it.

---

# **11. Example Full Session**

```
> add-note
Title: Pelvis anatomy
Content:
The pelvis tilts anteriorly in most neutral poses...
<empty line>

Tags: anatomy
Saved note #1

> ai-summarize-note 1
(AI summary appears)

> add-task
Title: Ribcage rotation study
Description: 15 drawings from reference
Priority: medium
Category: anatomy
Due date: 2025-11-30
Saved task #1

> ai-generate-practice 1
(AI drills appear)

> ai-critique A standing male figure viewed from above...
(AI critique appears)

> ai-anatomy eagle wing
(Full biomechanical breakdown appears)

> exit
```

---

# **12. What Prototype 3 Achieves**

Prototype 3 introduces major upgrades:

### PKMS + Tasks

✔ Better editing
✔ Tag filtering
✔ Stronger search
✔ In-progress workflow
✔ Safer delete
✔ Timestamps everywhere

### AI Features (5 Agents)

✔ Note summarizer
✔ Task practice generator
✔ Skill analysis with learning plan
✔ Mentor for any art question
✔ Ultra-detailed anatomical engine
✔ Industry-level art critique system

Prototype 3 is now a **fully capable art growth ecosystem**, not just a PKMS.

---
