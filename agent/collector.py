from integrations.calendar_client import list_upcoming_events

def collect_context():
    # TODO - Pull emails and all.
    calendar_events = list_upcoming_events(time_window_hours=24)

    return {
        "calendar": calendar_events,
        "preferences": {
            "auto_block_focus": True,
            "work_hours": {"start": "10:00", "end": "19:00"},
        }
    }
