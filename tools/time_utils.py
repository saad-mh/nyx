from datetime import datetime

def current_datetime() -> str:
    """
    returns the current date and time as a formatted string.

    :return: Description
    :rtype: str
    """
    return datetime.now().astimezone().strftime("%Y-%m-%d %H:%M:%S %Z")

# print("current datetime: ", current_datetime())

def current_date() -> str:
    """
    returns the current date in ISO format.
    
    :return: Description
    :rtype: str
    """
    return datetime.now().date().isoformat()

# print("current date: ", current_date())

def current_time(format_24: bool = True) -> str:
    """
    returns the current time as a formatted string.

    :return: Description
    :rtype: str
    """
    return datetime.now().time().strftime("%H:%M:%S") if format_24 else datetime.now().time().strftime("%I:%M:%S %p")

# print("current time: ", current_time(format_24=False))

def timestamp() -> int:
    """
    returns the current timestamp as an integer.

    :return: Description
    :rtype: int
    """
    return int(datetime.now().timestamp())

# print("current timestamp: ", timestamp())

def current_timezone():
    """
    returns the current timezone name.
    """
    return datetime.now().astimezone().tzname()

# print("current timezone: ", current_timezone())