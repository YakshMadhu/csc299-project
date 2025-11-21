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
