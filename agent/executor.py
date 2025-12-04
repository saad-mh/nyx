import json
from integrations.calendar_client import create_event, update_event, get_calendar_service

def cancel_event(event_id: str):
    service = get_calendar_service()
    service.events().delete(calendarId="primary", eventId=event_id).execute()


def execute_actions(actions_json):
    try:
        actions = json.loads(actions_json)
        if isinstance(actions, dict):
            actions = [actions]
    except Exception as e:
        return {"error": f"Invalid JSON from planner: {e}", "raw": actions_json}

    results = []

    for action in actions:
        atype = action.get("type")
        risk = action.get("risk", "medium")
        needs_confirm = action.get("requires_confirmation", True)

        # For now: only auto-run low-risk non-confirm actions
        if risk != "low" or needs_confirm:
            results.append({
                "status": "skipped_needs_confirmation",
                "action": action
            })
            continue

        try:
            if atype == "CREATE_EVENT":
                event_id = create_event(action["data"])
                results.append({"status": "created", "event_id": event_id, "action": action})

            elif atype == "UPDATE_EVENT":
                event_id = update_event(
                    action["data"]["event_id"],
                    action["data"]["updates"]
                )
                results.append({"status": "updated", "event_id": event_id, "action": action})

            elif atype == "CANCEL_EVENT":
                cancel_event(action["data"]["event_id"])
                results.append({"status": "cancelled", "action": action})

            elif atype == "NONE":
                results.append({"status": "no_op", "action": action})

            else:
                results.append({"status": "unknown_type", "action": action})

        except Exception as e:
            results.append({"status": "error", "error": str(e), "action": action})

    return results
