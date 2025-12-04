from __future__ import print_function
import datetime
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# rw access
SCOPES = ["https://www.googleapis.com/auth/calendar"]

TOKEN_PATH = "token.json"
CREDENTIALS_PATH = "credentials.json"


def get_calendar_service():
    creds = None
    if os.path.exists(TOKEN_PATH):
        creds = Credentials.from_authorized_user_file(TOKEN_PATH, SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                CREDENTIALS_PATH, SCOPES
            )
            creds = flow.run_local_server(port=0)
        with open(TOKEN_PATH, "w") as token:
            token.write(creds.to_json())

    service = build("calendar", "v3", credentials=creds)
    return service


def list_upcoming_events(max_results=20, time_window_hours=24):
    service = get_calendar_service()
    now = datetime.datetime.utcnow()
    time_min = now.isoformat() + "Z"
    time_max = (now + datetime.timedelta(hours=time_window_hours)).isoformat() + "Z"

    events_result = service.events().list(
        calendarId="primary",
        timeMin=time_min,
        timeMax=time_max,
        maxResults=max_results,
        singleEvents=True,
        orderBy="startTime",
    ).execute()

    events = events_result.get("items", [])
    normalized = []

    for e in events:
        start = e.get("start", {})
        end = e.get("end", {})
        normalized.append({
            "id": e.get("id"),
            "summary": e.get("summary", ""),
            "description": e.get("description", ""),
            "start": start.get("dateTime") or start.get("date"),
            "end": end.get("dateTime") or end.get("date"),
            "location": e.get("location", ""),
            "attendees": [a.get("email") for a in e.get("attendees", [])],
        })

    return normalized


def create_event(event_data: dict):
    """
    event_data example:
    {
      "summary": "Meeting with X",
      "description": "Discuss project",
      "start": "2025-12-05T15:00:00+05:30",
      "end":   "2025-12-05T16:00:00+05:30",
      "location": "Google Meet",
      "attendees": ["abc@example.com"]
    }
    """
    service = get_calendar_service()
    body = {
        "summary": event_data["summary"],
        "description": event_data.get("description", ""),
        "start": {"dateTime": event_data["start"]},
        "end": {"dateTime": event_data["end"]},
    }

    if event_data.get("location"):
        body["location"] = event_data["location"]
    if event_data.get("attendees"):
        body["attendees"] = [{"email": a} for a in event_data["attendees"]]

    created = service.events().insert(calendarId="primary", body=body).execute()
    return created.get("id")


def update_event(event_id: str, updates: dict):
    """
    updates: same fields as create_event but partial allowed
    """
    service = get_calendar_service()
    event = service.events().get(calendarId="primary", eventId=event_id).execute()

    if "summary" in updates:
        event["summary"] = updates["summary"]
    if "description" in updates:
        event["description"] = updates["description"]
    if "start" in updates:
        event["start"]["dateTime"] = updates["start"]
    if "end" in updates:
        event["end"]["dateTime"] = updates["end"]
    if "location" in updates:
        event["location"] = updates["location"]

    updated = service.events().update(
        calendarId="primary", eventId=event_id, body=event
    ).execute()
    return updated.get("id")
