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
