# llm/query.py
import ollama
from tools import time_utils

SYSTEM_PROMPT = """
You are Nyx, a local personal assistant.

Your job:
- Understand the user's intent
- Decide if a tool is needed
- If a tool is needed, output a JSON tool call
- Otherwise respond normally in plain text

Rules:
- Only output JSON when calling a tool
- JSON format:
  {"tool": "<tool_name>", "args": {...}}
- Do not calculate numbers yourself
- Do not guess dates or measurements
- Be concise

"""

def ask_model(prompt: str, model: str = "phi"):
    """
    Sends a prompt to a local Ollama model and returns raw text output.
    """
    time_now = time_utils.current_datetime()

    messages = [
        {
            "role": "system",
            "content": SYSTEM_PROMPT + f"\nCurrent system datetime: {time_now}"
        },
        {
            "role": "user",
            "content": prompt
        }
    ]

    response = ollama.chat(
        model=model,
        messages=messages
    )

    return response["message"]["content"].strip()
