from llm.query import ask_model

def plan(analysis):
    prompt = f"""
You are Nyx, an autonomous background assistant managing the user's calendar.

Given this analysis:

{analysis}

Propose a list of calendar actions in strict JSON.

Each action must be an object with:
- "type": one of ["CREATE_EVENT", "UPDATE_EVENT", "CANCEL_EVENT", "NONE"]
- "risk": "low" | "medium" | "high"
- "requires_confirmation": true/false
- "reason": short text
- "data": object with fields depending on type.

For CREATE_EVENT:
  "data": {{
    "summary": string,
    "description": string,
    "start": ISO8601 string with timezone,
    "end": ISO8601 string with timezone,
    "location": string or null,
    "attendees": [email strings] or []
  }}

For UPDATE_EVENT:
  "data": {{
    "event_id": string,
    "updates": {{
      "summary"?: string,
      "description"?: string,
      "start"?: ISO8601 string,
      "end"?: ISO8601 string,
      "location"?: string
    }}
  }}

For CANCEL_EVENT:
  "data": {{
    "event_id": string
  }}

If no action is needed, return a single item with:
  {{
    "type": "NONE",
    "risk": "low",
    "requires_confirmation": false,
    "reason": "No meaningful changes.",
    "data": {{}}
  }}

Respond with JSON only, no markdown, no explanations.
"""

    text, meta = ask_model(prompt)
    return text, meta


def analyze(context):
    prompt = f"""
You are Nyx, a background autonomous assistant.

Analyze the user's calendar context and identify:
- conflicts
- gaps
- risks
- opportunities

Context:
{context}

Respond ONLY in this format:

<analysis>
- ...
<potential_actions>
- ...
<missing_information>
- ...
"""
    text, meta = ask_model(prompt)
    return text, meta
