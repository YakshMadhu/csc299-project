Complete README.md for Task 4

# CSC299 – Task 4: OpenAI Chat Completions Summarizer

## Overview
This project is a **standalone Python experiment** exploring the OpenAI Chat Completions API.  
It takes multiple paragraph-length task descriptions and summarizes each one into a **short, clear phrase** using the `gpt-5-mini` model.  

Unlike earlier PKMS tasks, this one focuses solely on **API integration, looping logic**, and **output clarity**,  
rather than task or project management systems.

---

##  How to Run the Code

### 1️Open the Project
Open the `tasks4` folder in VS Code.  
Your structure should look like this:


tasks4/
│
├── src/
│ └── tasks4/
│ ├── init.py
│ └── main.py
│
├── pyproject.toml
├── .python-version
├── README.md
└── .gitignore


### 2️ Install dependencies (with uv)
In Git Bash (inside the `tasks4` folder):
```bash
uv sync


This creates a .venv environment and installs dependencies.

3️ Add your OpenAI API Key

Create a file named .env inside tasks4/ and add:

OPENAI_API_KEY=sk-your-real-key-here


This file is ignored by Git (listed in .gitignore) to protect your secret key.

4️ Run the summarizer
uv run tasks4


You should see:

Ready to Summarize, Ready to Summarize, Ready....

Task 1 summary: [short phrase here]
------------------------------------------------------------
Task 2 summary: [short phrase here]


Each task summary will be printed in clear, concise form.

 How This Was Built
 Step-by-Step Development

Initialized the folder using:

uv init


Created the project structure manually:

src/tasks4/__init__.py
src/tasks4/main.py


Configured pyproject.toml with:

[project.scripts]
tasks4 = "tasks4.main:main"


Wrote a Python script that:

imports OpenAI from the openai library

defines a list of paragraph samples

loops through them

uses client.chat.completions.create()

prints out each summarized response

Added environment variable handling via dotenv.

Verified the code locally using uv run tasks4.

Example Output
Task 1 summary: The rhythm of a city's day from dawn to night.
------------------------------------------------------------
Task 2 summary: A frog learns gratitude through hardship and nature.

💭 Reflection

This task taught me how to integrate and use the OpenAI Chat Completions API effectively within a Python package.
It was my first time experimenting with model-based summarization directly from code,
and I learned how to manage environment variables securely with .env and .gitignore.

Compared to previous tasks (Task 1–3), which were focused on building a personal knowledge management system (PKMS),
Task 4 was more experimental and exploratory — it showed how to design a clean API call flow, handle loops, and process model outputs efficiently.

One key takeaway was understanding the importance of clean project structure and dependency isolation.
Using uv, separating src/ logic, and following Python packaging conventions helped me see how production-grade projects are organized.
Finally, encountering GitHub push protection also taught me about security hygiene —
never committing API keys, using .gitignore properly, and ensuring version control safety.

🧾 Technologies Used

Python 3.14

OpenAI Python SDK

dotenv

uv (dependency management and runtime)

VS Code

Git + GitHub
