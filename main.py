from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime

from agent.collector import collect_context
from agent.reasoning import analyze, plan
from agent.executor import execute_actions
from agent.logger import log_update

from llm.qnyx import ask_model, sessions

import json
import time
import ollama
import threading

def run_agent():
    try:
        context = collect_context()
        analysis = analyze(context)
        actions = plan(analysis)
        results = execute_actions(actions)
        log_update(context, analysis, actions, results)
    except Exception as e:
        print("[NYX] Runtime error:", e)

def warmup_model():
    sessions.clear()
    print("[NYX] [dbg] Warming up Mistral")
    ollama.chat(
        model="mistral-nemo",
        messages=[{"role": "system", "content": "Initialize Nyx. Ignore this message."}]
    )
    print("[NYX] [dbg] Mistral is ready.")

def listen_for_commands():
    print("[NYX] [dbg] Command listener active.")
    
    while True:
        user_input = input("> ").strip()

        # Exit handler
        if user_input.lower() in ["exit", "quit"]:
            print("[NYX] Command listener shutting down.")
            break

        # Manual reset command
        if user_input.lower() in ["reset nyx", "nyx reset", "reset assistant"]:
            sessions.clear()
            print("[NYX]: Nyx has been reset and is ready.")
            continue

        # Inject current system datetime
        t_now = datetime.now().astimezone().strftime("%Y-%m-%d %H:%M:%S %Z")

        # Ask model (stateless)
        response, meta = ask_model(
            user_input,
            keep_history=False,
            timeNow=t_now
        )

        # Detect tool calls
        if response.strip().startswith("{") and "\"tool\"" in response:
            try:
                tool_call = json.loads(response)

                if tool_call.get("tool") == "days_until":
                    from agent.tools import days_until

                    current_date = t_now.split(" ")[0]
                    result = days_until(
                        tool_call["args"]["date_str"],
                        now_override=current_date
                    )

                    print(f"[NYX]: {result} days")
                    continue

            except Exception as e:
                print(f"[NYX]: Tool execution error: {e}")
                continue

        # Default response
        print(f"[NYX]: {response}")

if __name__ == "__main__":
    print("[NYX] [dbg] Initializing scheduler")
    warmup_model()

    listener_thread = threading.Thread(target=listen_for_commands, daemon=True)
    listener_thread.start()

    scheduler = BackgroundScheduler()
    # scheduler.add_job(run_agent, "interval", minutes=30)
    scheduler.start()

    print("[NYX] [dbg] Scheduler running. Press ctrl+c to stop.")

    try:
        while True:
            time.sleep(5)
    except KeyboardInterrupt:
        scheduler.shutdown()
        print("[NYX] [dbg] Shutdown complete.")
