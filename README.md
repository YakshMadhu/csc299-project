# Overview
This project revolves around the use of AI-coding assistants to plan, specify, develop, and test your own software that includes:
personal knowledge management system (PKMS)
personal task management system
a terminal-based chat interface to interact with your stored knowledge and tasks
AI agents that interact with the stored knowledge or tasks
The software must be written in Python and must run portably on Windows, macOS, and Linux.
Your state should be stored in JSON documents, a SQLite database, or a Neo4J database.

***For all of these deadlines, you should have your code committed and pushed to the GitHub repository by the due date***

# Timeline
-----------------------------------------------------------------------------------------------------------------------------
# Due [2025-09-22 Mon]
Try Notion and Obsidian
Create your public GitHub repo named csc299-project
Discuss this project with your favorite LLM
ask for ideas
Ask for a study plan for concepts to learn
ask for prototypes
Save those conversations in your GitHub repo
____________________________________________________________________________________________________________________________

# Due [2025-10-08 Wed]
ensure that you have tried out the diff, patch, and git experiments performed in teaching plans and lectures
It is critical to become comfortable with git before we develop larger examples
____________________________________________________________________________________________________________________________

# Due [2025-10-13 Mon]
Ensure that your public GitHub repo named csc299-project is shared with GitHub user bcdroid
Use exactly the name csc299-project (no variations with capitalization; rename your repository on GitHub if necessary)
_____________________________________________________________________________________________________________________________

# Due [2025-10-20 Mon]
Create a prototype command-line application that allows storing, listing, and searching tasks stored in a JSON data file
Put the code into files underneath a directory tasks1 in your csc299-project repository
Add a README.md file with instructions for running your code inside the tasks1 directory
so your csc299-project repository should have a tasks1 directory, and Python file(s) plus a README.md file inside that tasks1 directory
Make sure that your commits are in your public GitHub repo (not just your local repository)
_____________________________________________________________________________________________________________________________

# Due [2025-11-03 Mon]
iterate on the development of your PKMS/task software
Put your new code into a new tasks2 directory in your csc299-project repository
_____________________________________________________________________________________________________________________________

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
____________________________________________________________________________________________________________________________

# Due [2025-11-10 Mon]
Create a new tasks4 directory and Python package in your repository using uv as before
This is a standalone experiment to try out the OpenAI Chat Completions API, so you do not need to copy over any of your PKMS/task software
Use the OpenAI Chat Completions API to send a paragraph-length description of a task to ChatGPT-5-mini and have it summarize the task as a short phrase
Add a loop to your code so that it can summarize multiple paragraph-length descriptions (independently of one another)
Add at least 2 sample paragraph-length descriptions to your code so that running uv run tasks4 will summarize both descriptions and then print the summaries
_____________________________________________________________________________________________________________________________
# Due [2025-11-19 Wed]
Install GitHub's spec-kit from https://github.com/github/spec-kit
Watch the lecture from Wednesday, November 12, 2025, if you have not already done so.
Use spec-kit to create your own version of the tasks manager built in class.
You should build it in a new Git repository so that you do not have any confusion between the new code generated from the spec-kit and your existing code.
When you are done, copy everything from the new git repository (except the .git folder) into a tasks5 directory in your csc299-project repository, then commit and push.
_____________________________________________________________________________________________________________________________

# Due [2025-11-24 Mon] at 1:30 PM - Final Project Deadline
Make sure that all of your work is on GitHub at this time
Your GitHub repository will be pulled at this time
hard deadline: no changes after this time will be used/accepted for grading
_____________________________________________________________________________________________________________________________



