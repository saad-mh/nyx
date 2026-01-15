from datetime import date, datetime, timedelta

def days_between(start: date, end: date) -> int:
    """
    returns how many days are there between two dates.
    
    :param start: Description
    :type start: date
    :param end: Description
    :type end: date
    :return: Description
    :rtype: int
    """
    delta = end - start
    return abs(delta.days)

def days_until(target: date) -> int:
    """
    returns the number of days from today until the target date.
    
    :param target: Description
    :type target: date
    :return: Description
    :rtype: int
    """
    today = date.today()
    delta = target - today
    return delta.days

def is_valid_date(date_str: str) -> bool:
    """
    checks if a string is a valid date in YYYY-MM-DD format. Used before passing arguements to other functions to check for sanity.
    
    :param date_str: Description
    :type date_str: str
    :return: Description
    :rtype: bool
    """
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except:
        return False

def add_days(start: date, days: int) -> date:
    """
    Add a number of days to a given date.
    
    :return: Description
    :rtype: date
    """
    return start + timedelta(days=days)

def subtract_days(start: date, days: int) -> date:
    """
    Subtract a number of days from a given date.

    :return: Description
    :rtype: date
    """
    return start - timedelta(days=days)

