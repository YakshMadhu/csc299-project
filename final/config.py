# final/config.py
import os

# Set this in your environment:
#   macOS/Linux:  export OPENAI_API_KEY="sk-..."
#   Windows PS:   $env:OPENAI_API_KEY="sk-..."
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

# Use whatever model your class is using; adjust if needed.
OPENAI_MODEL = "gpt-5.1-mini"