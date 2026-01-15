TOOLS = {
    "date_utils": {
        "description": "A collection of date-related utility functions.",
        "path": "tools/date_calculator.py",
        "functions": {
            "days_between": {
                "description": "Returns how many days are there between two dates.",
                "args": [{"start": "date"}, {"end": "date"}],
                "return_type": "int"
            },
            "days_until": {
                "description": "Returns the number of days from today until the target date.",
                "args": [{"target": "date"}],
                "return_type": "int"
            },
            "is_valid_date": {
                "description": "Checks if a string is a valid date in YYYY-MM-DD format.",
                "args": [{"date_str": "str"}],
                "return_type": "bool"
            },
            "add_days": {
                "description": "Add a number of days to a given date.",
                "args": [{"start": "date"}, {"days": "int"}],
                "return_type": "date"
            },
            "subtract_days": {
                "description": "Subtract a number of days from a given date.",
                "args": [{"start": "date"}, {"days": "int"}],
                "return_type": "date"
            },
            "is_weekend": {
                "description": "Checks if the given date falls on a weekend (Saturday or Sunday).",
                "args": [{"target_date": "date"}],
                "return_type": "bool"
            }
        }
    },
    "time_utils": {
        "description": "A collection of time-related utility functions.",
        "path": "tools/time_utils.py",
        "functions": {
            "current_datetime": {
                "description": "Returns the current date and time in ISO format.",
                "args": [],
                "return_type": "str"
            },
            "current_date": {
                "description": "Returns the current date in ISO format.",
                "args": [],
                "return_type": "str"
            },
            "current_month": {
                "description": "Returns the current month as a string.",
                "args": [],
                "return_type": "str"
            },
            "current_year": {
                "description": "Returns the current year as an integer.",
                "args": [],
                "return_type": "int"
            },
            "current_time": {
                "description": "Returns the current time as a formatted string.",
                "args": [{"format_24": "bool"}],
                "return_type": "str"
            },
            "timestamp": {
                "description": "Returns the current timestamp as an integer.",
                "args": [],
                "return_type": "int"
            },
            "current_timezone": {
                "description": "Returns the current timezone as a string.",
                "args": [],
                "return_type": "str"
            },
            "seconds_between": {
                "description": "Returns how many seconds are there between two datetime objects.",
                "args": [{"start": "datetime"}, {"end": "datetime"}],
                "return_type": "int"
            },
            "add_seconds": {
                "description": "Add a number of seconds to a given datetime.",
                "args": [{"start": "datetime"}, {"seconds": "int"}],
                "return_type": "datetime"
            },
            "subtract_seconds": {
                "description": "Subtract a number of seconds from a given datetime.",
                "args": [{"start": "datetime"}, {"seconds": "int"}],
                "return_type": "datetime"
            }
        }
    },
    "math_utils": {
        "description": "A collection of mathematical utility functions.",
        "path": "tools/math_utils.py",
        "functions": {
            "factorial": {
                "description": "Returns the factorial of a non-negative integer n.",
                "args": [{"n": "int"}],
                "return_type": "int"
            },
            "is_prime": {
                "description": "Returns True if n is prime, False otherwise.",
                "args": [{"n": "int"}],
                "return_type": "bool"
            },
            "logarithm": {
                "description": "Returns the logarithm of a value with the specified base.",
                "args": [{"value": "float"}, {"base": "float"}],
                "return_type": "float"
            },
            "sqrt": {
                "description": "Returns the square root of a non-negative value.",
                "args": [{"value": "float"}],
                "return_type": "float"
            },
            "power": {
                "description": "Returns the result of raising base to the exponent power.",
                "args": [{"base": "float"}, {"exponent": "float"}],
                "return_type": "float"
            },
            "add": {
                "description": "Returns the sum of two numbers.",
                "args": [{"a": "float"}, {"b": "float"}],
                "return_type": "float"
            },
            "subtract": {
                "description": "Returns the difference of two numbers.",
                "args": [{"a": "float"}, {"b": "float"}],
                "return_type": "float"
            },
            "multiply": {
                "description": "Returns the product of two numbers.",
                "args": [{"a": "float"}, {"b": "float"}],
                "return_type": "float"
            },
            "divide": {
                "description": "Returns the quotient of two numbers. Returns -1 if division by zero",
                "args": [{"a": "float"}, {"b": "float"}],
                "return_type": "float"
            },
            "sine": {
                "description": "Returns the sine of an angle in radians.",
                "args": [{"angle_rad": "float"}],
                "return_type": "float"
            },
            "cosine": {
                "description": "Returns the cosine of an angle in radians.",
                "args": [{"angle_rad": "float"}],
                "return_type": "float"
            },
            "tangent": {
                "description": "Returns the tangent of an angle in radians.",
                "args": [{"angle_rad": "float"}],
                "return_type": "float"
            },
        }
    },
    "memory": {
        "description": "A simple in-memory key-value store.",
        "path": "tools/memory_store.py",
        "functions": {
            "remember": {
                "description": "Stores a value with the associated key.",
                "args": [{"key": "str"}, {"value": "any"}],
                "return_type": "None"
            },
            "recall": {
                "description": "Retrieves the value associated with the given key.",
                "args": [{"key": "str"}],
                "return_type": "any"
            },
            "forget": {
                "description": "Removes the value associated with the given key.",
                "args": [{"key": "str"}],
                "return_type": "None"
            },
            "list_memory": {
                "description": "Lists all key-value pairs stored in memory.",
                "args": [],
                "return_type": "dict"
            },
            "clear_memory": {
                "description": "Clears all entries from the memory store.",
                "args": [],
                "return_type": "None"
            }
        },
    },
    "system_info": {
        "description": "Retrieves basic system information.",
        "path": "tools/system_info.py",
        "functions": {
            "system_status": {
                "description": "Returns the operating system, hostname, and current user.",
                "args": [],
                "return_type": "dict"
            }
        }
    },
    "task_manager": {
        "description": "A simple task management utility.",
        "path": "tools/task_manager.py",
        "functions": {
            "add_task": {
                "description": "Adds a new task to the task list.",
                "args": [{"task": "str"}],
                "return_type": "None"
            },
            "list_tasks": {
                "description": "Lists all tasks in the task list.",
                "args": [],
                "return_type": "list"
            },
            "remove_task": {
                "description": "Removes a task from the task list by its index.",
                "args": [{"index": "int"}],
                "return_type": "None"
            },
            "clear_tasks": {
                "description": "Clears all tasks from the task list.",
                "args": [],
                "return_type": "None"
            }
        }
    },
    "text_utils": {
        "description": "A collection of text manipulation utility functions.",
        "path": "tools/text_utils.py",
        "functions": {
            "word_count": {
                "description": "Returns the number of words in the given text.",
                "args": [{"text": "str"}],
                "return_type": "int"
            },
            "summarize_length": {
                "description": "Returns a summary of the text length including character and word counts.",
                "args": [{"text": "str"}],
                "return_type": "dict"
            },
            "reverse_text": {
                "description": "Reverses the given text string.",
                "args": [{"text": "str"}],
                "return_type": "str"
            }
        }
    },
    "conversion_utils": {
        "description": "A collection of unit conversion utility functions.",
        "path": "tools/conversion.py",
        "functions": {
            "mm2cm": {
                "description": "Convert millimeters to centimeters.",
                "args": [{"mm": "float"}],
                "return_type": "float"
            },
            "cm2mm": {
                "description": "Convert centimeters to millimeters.",
                "args": [{"cm": "float"}],
                "return_type": "float"
            },
            "inches2cm": {
                "description": "Convert inches to centimeters.",
                "args": [{"inches": "float"}],
                "return_type": "float"
            },
            "cm2inches": {
                "description": "Convert centimeters to inches.",
                "args": [{"cm": "float"}],
                "return_type": "float"
            },
            "pounds2kg": {
                "description": "Convert pounds to kilograms.",
                "args": [{"pounds": "float"}],
                "return_type": "float"
            },
            "kg2pounds": {
                "description": "Convert kilograms to pounds.",
                "args": [{"kg": "float"}],
                "return_type": "float"
            },
            "fahrenheit2celsius": {
                "description": "Convert Fahrenheit to Celsius.",
                "args": [{"fahrenheit": "float"}],
                "return_type": "float"
            },
            "celsius2fahrenheit": {
                "description": "Convert Celsius to Fahrenheit.",
                "args": [{"celsius": "float"}],
                "return_type": "float"
            },
            "liters2gallons": {
                "description": "Convert liters to gallons.",
                "args": [{"liters": "float"}],
                "return_type": "float"
            },
            "gallons2liters": {
                "description": "Convert gallons to liters.",
                "args": [{"gallons": "float"}],
                "return_type": "float"
            },
            "radians2degrees": {
                "description": "Convert radians to degrees.",
                "args": [{"radians": "float"}],
                "return_type": "float"
            },
            "degrees2radians": {
                "description": "Convert degrees to radians.",
                "args": [{"degrees": "float"}],
                "return_type": "float"
            }
        }
    }
}