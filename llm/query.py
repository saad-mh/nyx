from openai import OpenAI
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


def ask_model(prompt: str, model: str = "gpt-4.1-mini"):
    response = client.responses.create(
        model=model,
        input=[
            {
                "role": "user",
                "content": prompt
            }
        ],
    )

    text = _extract_text(response)

    usage = getattr(response, "usage", None)

    cost_inr, in_toks, out_toks = _calculate_cost(model, usage)

    meta = {
        "model": model,
        "input_tokens": in_toks,
        "output_tokens": out_toks,
        "cost_inr": cost_inr
    }

    return text, meta
