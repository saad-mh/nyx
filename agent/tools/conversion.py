import math

def mm2cm(mm: float) -> float:
    """
    Convert millimeters to centimeters.
    
    :param mm: Description
    :type mm: float
    :return: Description
    :rtype: float
    """
    return mm / 10.0

def cm2mm(cm: float) -> float:
    """
    Convert centimeters to millimeters.
    
    :param cm: Description
    :type cm: float
    :return: Description
    :rtype: float
    """
    return cm * 10.0

def inches2cm(inches: float) -> float:
    """
    Convert inches to centimeters.
    
    :param inches: Description
    :type inches: float
    :return: Description
    :rtype: float
    """
    return inches * 2.54

def cm2inches(cm: float) -> float:
    """
    Convert centimeters to inches.
    
    :param cm: Description
    :type cm: float
    :return: Description
    :rtype: float
    """
    return cm / 2.54

def pounds2kg(pounds: float) -> float:
    """
    Convert pounds to kilograms.
    
    :param pounds: Description
    :type pounds: float
    :return: Description
    :rtype: float
    """
    return pounds * 0.453592

def kg2pounds(kg: float) -> float:
    """
    Convert kilograms to pounds.
    
    :param kg: Description
    :type kg: float
    :return: Description
    :rtype: float
    """
    return kg / 0.453592

def fahrenheit2celsius(fahrenheit: float) -> float:
    """
    Convert Fahrenheit to Celsius.
    
    :param fahrenheit: Description
    :type fahrenheit: float
    :return: Description
    :rtype: float
    """
    return (fahrenheit - 32) * 5.0 / 9.0

def celsius2fahrenheit(celsius: float) -> float:
    """
    Convert Celsius to Fahrenheit.
    
    :param celsius: Description
    :type celsius: float
    :return: Description
    :rtype: float
    """
    return (celsius * 9.0 / 5.0) + 32

def liters2gallons(liters: float) -> float:
    """
    Convert liters to gallons.
    
    :param liters: Description
    :type liters: float
    :return: Description
    :rtype: float
    """
    return liters * 0.264172

def gallons2liters(gallons: float) -> float:
    """
    Convert gallons to liters.
    
    :param gallons: Description
    :type gallons: float
    :return: Description
    :rtype: float
    """
    return gallons / 0.264172

def radians2degrees(radians: float) -> float:
    return math.degrees(radians)

def degrees2radians(degrees: float) -> float:
    return math.radians(degrees)