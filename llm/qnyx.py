import ollama
import re

sessions = {}

TOOL_JSON_FORMAT = "{{\"tool\": \"days_until\", \"args\": {{\"date_str\": \"YYYY-MM-DD\"}}}}"

global_system_prompt = f"""
You are Nyx, Saad's fast and local personal assistant.

Rules:

1. DATE DIFFERENCE QUESTIONS:
   You MUST output ONLY this JSON format for countdown-type questions:

   {TOOL_JSON_FORMAT}

   Countdown questions include phrases like:
   - "how many days until"
   - "how many days to"
   - "days until"
   - "days to"
   - "countdown to"
   DO NOT output natural language for these.

2. TIME QUESTIONS:
   For "what time is it" → respond ONLY using CURRENT SYSTEM DATETIME.

3. DATE QUESTIONS:
   For "what date is it" → respond ONLY using CURRENT SYSTEM DATETIME.

4. EVERYTHING ELSE:
   Respond normally in natural language.
   DO NOT output JSON.
   DO NOT output tool calls.
   DO NOT guess or calculate dates.
"""


def is_countdown_query(prompt: str):
    p = prompt.lower()
    return bool(re.search(r"(how many days|days until|days to|countdown)", p))


def ask_model(
    prompt: str,
    model: str = "mistral-nemo",
    keep_history: bool = False,
    timeNow: str = ""
):
    system_prompt = {
        "role": "system",
        "content": global_system_prompt
                  + f"\nCURRENT SYSTEM DATETIME (DO NOT IGNORE): {timeNow}\n"
    }
    if not keep_history:
        messages_to_send = [
            system_prompt,
            {"role": "user", "content": prompt}
        ]
    else:
        if model not in sessions:
            sessions[model] = [system_prompt]

        sessions[model].append({"role": "user", "content": prompt})
        messages_to_send = sessions[model]

    response = ollama.chat(model=model, messages=messages_to_send)
    output = response["message"]["content"].strip()

    if keep_history:
        sessions[model].append({"role": "assistant", "content": output})

    return output, {}
