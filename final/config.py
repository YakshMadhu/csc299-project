# final/config.py
import os

# Set this in your environment:
#   macOS/Linux:  export OPENAI_API_KEY="sk-..."
#   Windows PS:   $env:OPENAI_API_KEY="sk-..."
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
OPENAI_MODEL = "gpt-4o"