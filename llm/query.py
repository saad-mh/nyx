from openai import OpenAI
import subprocess
import json
from config import OPENAI_API_KEY, MODEL_PRICING, USD_TO_INR

client = OpenAI(api_key=OPENAI_API_KEY)


def _extract_text(response) -> str:
    try:
        if not response.output:
            return ""

        out = response.output[0]

        if hasattr(out, "content") and out.content:
            for c in out.content:
                if hasattr(c, "text"):
                    return c.text

        if hasattr(out, "refusal"):
            return out.refusal

        return str(response)

    except Exception as e:
        return f"[NYX_LLM_PARSE_ERROR] {e}"


def _calculate_cost(model: str, usage):
    # If OpenAI did not return token usage, cost = 0 for now
    if usage is None:
        return 0.0, 0, 0

    if model not in MODEL_PRICING:
        return 0.0, 0, 0

    inp_tokens = getattr(usage, "input_tokens", 0)
    out_tokens = getattr(usage, "output_tokens", 0)

    price = MODEL_PRICING[model]

    cost_usd = (
        (inp_tokens / 1_000_000) * price["input_per_million"] +
        (out_tokens / 1_000_000) * price["output_per_million"]
    )

    cost_inr = cost_usd * USD_TO_INR

    return round(cost_inr, 4), inp_tokens, out_tokens


def ask_model(prompt: str, model: str = "mistral-nemo"):
    """
    Primary model used for all lightweight reasoning and routing.
    """
    text = run_ollama(model, prompt)
    meta = {
        "model": model,
        "input_tokens": 0,    # we can approximate later
        "output_tokens": 0,
        "cost_inr": 0.0
    }

    return text, meta


def run_ollama(model: str, prompt: str):
    """
    Runs an Ollama model and returns pure text output.
    """
    try:
        result = subprocess.run(
            ["ollama", "run", model],
            input=prompt.encode("utf-8"),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            timeout=30
        )

        output = result.stdout.decode("utf-8").strip()
        return output

    except Exception as e:
        return f"[NYX/olm] [!] {e}"