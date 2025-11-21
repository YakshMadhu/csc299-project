# CSC299 Project Timeline

## Milestones

# 2025-09-22
- Try Notion and Obsidian.
- Create your public GitHub repo named csc299-project.
- Discuss this project with your favorite LLM.
- Ask for:
  - Study plan for concepts to learn
  - Ideas for prototypes  
- Save those conversations in your GitHub repo.

#  2025-10-08
- Ensure that you have tried out the diff, patch, and git experiments shown in class.  
- This helps you get comfortable with Git before starting larger examples.

#  2025-10-13
- Verify your public GitHub repo name is exactly csc299-project.  
- Share the repo with the GitHub Professor.  
- Rename your repository if the capitalization is incorrect.

# 2025-10-20
- Create a prototype command-line application that:
  - Stores, lists, and searches tasks using a JSON data file.
  - Keeps all code in a folder named tasks1 inside your repo.
  - Includes a README.md in the tasks1 folder with instructions for running the app.
- Make sure all commits are pushed to your public GitHub repo (not just saved locally).

# Due [2025-11-03 Mon]
iterate on the development of your PKMS/task software
Put your new code into a new tasks2 directory in your csc299-project repository

# Due [2025-11-05 Wed]
install uv
from your csc299-project directory, run uv init tasks3 --vcs none --package tasks3 to create a new tasks3 directory and initialize it is a Python package
Add pytest by running uv add --dev pytest inside the tasks3 directory
add this Python code to the top of tasks3/src/__init__.py

def inc(n: int) -> int:
    return n + 1
Create a file tests/test_inc.py with this Python code:

from tasks3 import inc

def test_inc():
    assert inc(5) == 6
Run uv run pytest to verify that your test setup is working correctly (it should say "1 passed")
Now incorporate some (at least 2) tests (using the pytest framework) into your PKMS/task software
call your code from the main method in tasks3/src/__init__.py
then your code can be started using uv run tasks3, which calls the main method in tasks3/src/__init__.py
you can copy your existing tasks2 code into tasks3 and then add tests, or you can start with new code for tasks3, whichever you prefer
precisely what you test is up to you, and depends upon what you have implemented so far
remember that you can access the book Python Testing with pytest, 2nd Edition for free via the DePaul library E-book collections and O'Reilly for Higher Education
here are some example repositories to help you get something working (the README.md in each one documents how the repository was created):
https://github.com/bcdroid/demo-pytest
https://github.com/bcdroid/demo-stdin-stdout-pytest
https://github.com/bcdroid/demo-typer
https://github.com/bcdroid/demo-typer-pytest
https://github.com/bcdroid/demo-chat
https://github.com/bcdroid/demo-chat-completions




