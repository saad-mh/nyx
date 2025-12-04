from apscheduler.schedulers.background import BackgroundScheduler
from agent.collector import collect_context
from agent.reasoning import analyze, plan
from agent.executor import execute_actions
from agent.logger import log_update
import time

def run_agent():
    try:
        context = collect_context()
        analysis = analyze(context)
        actions = plan(analysis)
        results = execute_actions(actions)
        log_update(context, analysis, actions, results)
    except Exception as e:
        print("[NYX] Runtime error: ", e)

if __name__ == "__main__":
    print("[NYX] [dbg] Initializing scheduler")

    scheduler = BackgroundScheduler()
    scheduler.add_job(run_agent, "interval", minutes=30)
    scheduler.start()

    print("[NYX] [dbg] Scheduler running. Press ctrl+c to stop.")

    try:
        while True:
            time.sleep(5)
    except KeyboardInterrupt:
        scheduler.shutdown()
        print("[NYX] [dbg] Shutdown complete.")
