from datetime import datetime, timedelta

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

def current_month() -> str:
    """
    returns the current month as a string.

    :return: Description
    :rtype: str
    """
    return datetime.now().strftime("%B")

# print("current month: ", current_month())

def current_year() -> int:
    """
    returns the current year as an integer.

    :return: Description
    :rtype: int
    """
    return datetime.now().year

# print("current year: ", current_year())


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

def seconds_between(start: datetime, end: datetime) -> int:
    """
    returns how many seconds are there between two datetime objects.
    
    :param start: Description
    :type start: datetime
    :param end: Description
    :type end: datetime
    :return: Description
    :rtype: int
    """
    delta = end - start
    return abs(int(delta.total_seconds()))

def add_seconds(start: datetime, seconds: int) -> datetime:
    """
    Add a number of seconds to a given datetime.
    
    :return: Description
    :rtype: datetime
    """
    return start + timedelta(seconds=seconds)

def subtract_seconds(start: datetime, seconds: int) -> datetime:
    """
    Subtract a number of seconds from a given datetime.

    :return: Description
    :rtype: datetime
    """
    return start - timedelta(seconds=seconds)

