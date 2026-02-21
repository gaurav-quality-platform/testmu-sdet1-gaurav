import os
from dotenv import load_dotenv

# force load .env from project root
load_dotenv(dotenv_path=".env")

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
MODEL = "openai/gpt-4o-mini"

if not OPENROUTER_API_KEY:
    raise ValueError("OPENROUTER_API_KEY not found. Check your .env file")