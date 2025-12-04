from llm.query import ask_model

def analyze(context):
    prompt = f"""
You are Nyx. Analyze this context and extract conflicts, risks,
and opportunities.

Context:
{context}
"""
    text, meta = ask_model(prompt, model="mistral-nemo")
    return text, meta


def plan(analysis):
    prompt = f"""
Plan actions in strict JSON based on this analysis:

{analysis}
"""
    text, meta = ask_model(prompt, model="mistral-nemo")
    return text, meta
