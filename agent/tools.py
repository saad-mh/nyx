from datetime import datetime
from typing import Optional

def days_until(date_str: str, now_override: Optional[str] = None) -> int:
    """
    Compute number of days from `now_override` (YYYY-MM-DD) or from system date
    to target `date_str` (YYYY-MM-DD). Returns an integer (can be negative).
    """
    target = datetime.strptime(date_str, "%Y-%m-%d").date()
    if now_override:
        try:
            today = datetime.strptime(now_override, "%Y-%m-%d").date()
        except Exception:
            try:
                today = datetime.fromisoformat(now_override.split(" ")[0]).date()
            except Exception:
                today = datetime.now().date()
    else:
        today = datetime.now().date()

    delta = (target - today).days
    return delta
