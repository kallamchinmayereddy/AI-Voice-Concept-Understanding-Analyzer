import os

# -----------------------------
# Gemini Configuration
# -----------------------------

GEMINI_MODEL = "gemini-2.5-flash"

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# -----------------------------
# Knowledge Base
# -----------------------------

KNOWLEDGE_BASE_PATH = "knowledge_base"

# -----------------------------
# Generation Settings
# -----------------------------

WORDS_PER_TOPIC = 500