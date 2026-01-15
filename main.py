import json
from llm.query import ask_model
from agent.registry import TOOLS as TOOL_REGISTRY
import importlib


def execute_tool(tool_name: str, args: dict):
    if tool_name not in TOOL_REGISTRY:
        raise ValueError("Tool not registered")

    tool_meta = TOOL_REGISTRY[tool_name]

    module = importlib.import_module(tool_meta["module"])
    func = getattr(module, tool_meta["function"])

    return func(**args)

def main():
    print("[NYX] Ready. Type 'exit' to quit.")

    while True:
        user_input = input("> ").strip()

        if user_input.lower() in ["exit", "quit"]:
            print("[NYX] Goodbye.")
            break

        output = ask_model(user_input)

        if output.startswith("{"):
            try:
                tool_call = json.loads(output)

                tool_name = tool_call.get("tool")
                args = tool_call.get("args", {})

                result = execute_tool(tool_name, args)
                print(f"[NYX]: {result}")

            except Exception as e:
                print("[NYX]: Tool error:", e)


if __name__ == "__main__":
    main()
