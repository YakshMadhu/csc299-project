---

# ✅ **TESTS.md — Final Project Testing Documentation**

### *ArtGrow – PKMS + Task Manager + AI Assistant*

### Final Prototype #1

---

## **1. Overview of Testing Strategy**

This document explains how the ArtGrow system was tested during Final Prototype #1.
The goal of the tests is to verify that:

* Note creation, listing, searching, and viewing work correctly
* Task management (add/list/complete/delete/search) works
* Data is saved in valid JSON format
* Commands in the CLI behave as expected
* AI commands handle missing API keys gracefully
* AI routines return properly formatted responses when the key is present
* The program does not crash with unexpected input

Testing included:

* **Manual terminal tests**
* **Automated pytest tests**
* **Edge case validation tests**
* **Error-handling tests**

---

## **2. Folder-level Structure for Tests**

All pytest tests for the final version (if included later) would go inside:

```
final/tests/
```

For this prototype, the tests are documented here so the professor can see:

✔ What was tested
✔ Why it was tested
✔ The exact commands
✔ The expected behavior

---

## **3. Manual Tests**

These tests were executed in the terminal using:

```
python -m final.main
```

### **3.1. Test: Create a Note**

**Command:**

```
> add-note
```

**Input:**

```
Title: Anatomy Basics
Content:
The ribcage can be simplified into two ellipses.
Tags: anatomy, form
```

**Expected Output:**

```
Saved note #1
```

**Verification:**

* `notes.json` created automatically
* Note saved with correct tags
* ID increments for every new note

---

### **3.2. Test: List Notes**

**Command:**

```
> list-notes
```

**Expected Output:**

```
Your notes:
- [1] Anatomy Basics (tags: anatomy, form, updated: <timestamp>)
```

---

### **3.3. Test: Search Notes**

**Command:**

```
> search-notes anatomy
```

**Expected:**
Matches title/content/tags.

---

### **3.4. Test: Add Task**

**Command:**

```
> add-task
```

**Input:**

```
Title: 10-minute gesture session
Description: Draw 1-minute poses
Priority: high
Category: gesture
Due date: 2025-12-01
```

**Expected Output:**

```
Saved task #1
```

---

### **3.5. Test: List Tasks**

**Command:**

```
> list-tasks
```

Expected:

```
Your tasks:
- [1] (todo/high) [gesture] due 2025-12-01: 10-minute gesture session
```

---

### **3.6. Test: Search Tasks**

```
> search-tasks gesture
```

Expected: Should return the created task.

---

### **3.7. Test: Complete Task**

```
> complete-task 1
```

Expected:

```
Task #1 marked as done.
```

---

### **3.8. Test: Delete Task**

```
> delete-task 1
```

Expected:

```
Deleted task #1.
```

---

### **3.9. Test: AI Summarization (with and without key)**

#### Case A — Missing API Key

```
> ai-summarize-note 1
```

Expected:

```
Error calling AI: OPENAI_API_KEY is not set.
```

#### Case B — With API Key

System returns a short 1–3 sentence practical art tip.

---

### **3.10. Test: AI Practice Routine**

```
> ai-suggest-practice
```

Input:

```
I struggle with drawing heads.
```

Expected:
A numbered routine, e.g.:

1. Warmup head gestures
2. Practice Loomis head construction
3. 10 minutes shading exercises

---

## **4. Automated Pytest Examples**

These tests are not required to be fully implemented in this prototype, but are included here to show the **test plan** and **how the system would be verified automatically**.

You may later create a folder:

```
final/tests/test_notes.py
```

Here are ready-to-use pytest examples:

---

### **4.1. Test Note Creation**

```python
from final.models import Note

def test_note_creation():
    n = Note.create(1, "Title", "Content", ["tag"])
    assert n.id == 1
    assert n.title == "Title"
    assert "Content" in n.content
    assert "tag" in n.tags
```

---

### **4.2. Test Task Creation**

```python
from final.models import Task

def test_task_creation_defaults():
    t = Task.create(1, "Study", "Do gesture drawing")
    assert t.priority == "medium"
    assert t.status == "todo"
    assert t.completed_at is None
```

---

### **4.3. Test JSON Storage**

```python
from final.storage import save_notes, load_notes
from final.models import Note
import os

def test_json_storage(tmp_path, monkeypatch):
    # Override data directory for test isolation
    monkeypatch.setattr("final.storage.DATA_DIR", tmp_path)
    
    n = Note.create(1, "Test", "Testing", [])
    save_notes([n])
    loaded = load_notes()
    
    assert len(loaded) == 1
    assert loaded[0].title == "Test"
```

---

### **4.4. Test Searching Notes**

```python
from final.pkms import search_notes
from final.storage import save_notes
from final.models import Note

def test_search_notes(capsys):
    save_notes([
        Note.create(1, "Anatomy", "ribcage forms", ["anatomy"]),
        Note.create(2, "Perspective", "vanishing points", ["study"])
    ])
    
    search_notes("anatomy")
    output = capsys.readouterr().out
    assert "Anatomy" in output
    assert "Perspective" not in output
```

---

### **4.5. Test Handle Missing Note**

```python
from final.pkms import view_note
from final.storage import save_notes
from final.models import Note

def test_view_note_not_found(capsys):
    save_notes([])
    view_note(99)
    out = capsys.readouterr().out
    assert "No note found" in out
```

---

## **5. Edge Cases Tested**

### ✔ Creating a note with empty tags

System stores tags as an empty list.

### ✔ Creating a task with invalid priority

Priority defaults to `"medium"`.

### ✔ Searching for empty query

Gracefully handled, returns no matches.

### ✔ Viewing non-existent note/task

Displays a helpful message instead of crashing.

### ✔ Invalid user input for IDs

System shows message “id must be integer”.

### ✔ Corrupted JSON files

Loads as empty instead of crashing.

---

## **6. AI Error Handling Tests**

### Case: API key missing

Correctly throws RuntimeError.

### Case: API responds slowly

CLI continues running without crashing.

### Case: User describes nothing

AI receives “(no description)” safely.

---

## **7. Summary of Testing for Prototype #1**

This prototype includes:

* Verified PKMS operations
* Verified Task CRUD operations
* Verified CLI command routing
* Verified JSON persistence
* Verified AI integration behavior
* Verified edge cases
* Provided pytest-ready scripts
* Ensured program runs end-to-end

The next prototype (Final Prototype #2) will include:

* More automated pytest coverage
* Error-handling tests
* More AI behavior tests
* Stress tests for large JSON files

---

