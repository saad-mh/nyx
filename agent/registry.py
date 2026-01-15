from datetime import date


TOOLS = {
    "days_between": {
        "description": "Returns how many days are there between two dates.",
        "module": "agent.tools.date_calculator",
        "function": "days_between",
        "args": {
            "start": "date",
            "end": "date"
        },
        "return_type": "int"
    },
    "days_until": {
        "description": "Returns the number of days from today until the target date.",
        "module": "agent.tools.date_calculator",
        "function": "days_until",
        "args": {
            "target": "date"
        },
        "return_type": "int"
    },
    "is_valid_date": {
        "description": "Checks if a string is a valid date in YYYY-MM-DD format.",
        "module": "agent.tools.date_calculator",
        "function": "is_valid_date",
        "args": {
            "date_str": "str"
        },
        "return_type": "bool"
    },
    "add_days": {
        "description": "Add a number of days to a given date.",
        "module": "agent.tools.date_calculator",
        "function": "add_days",
        "args": {
            "start": "date",
            "days": "int"
        },
        "return_type": "date"
    },
    "subtract_days": {
        "description": "Subtract a number of days from a given date.",
        "module": "agent.tools.date_calculator",
        "function": "subtract_days",
        "args": {
            "start": "date",
            "days": "int"
        },
        "return_type": "date"
    },
    "is_weekend": {
        "description": "Checks if the given date falls on a weekend (Saturday or Sunday).",
        "module": "agent.tools.date_calculator",
        "function": "is_weekend",
        "args": {
            "target_date": "date"
        },
        "return_type": "bool"
    },
    "current_datetime": {
        "description": "Returns the current date and time in ISO format.",
        "module": "agent.tools.time_utils",
        "function": "current_datetime",
        "args": {},
        "return_type": "str"
    },
    "current_date": {
        "description": "Returns the current date in ISO format.",
        "module": "agent.tools.time_utils",
        "function": "current_date",
        "args": {},
        "return_type": "str"
    },
    "current_month": {
        "description": "Returns the current month as a string.",
        "module": "agent.tools.time_utils",
        "function": "current_month",
        "args": {},
        "return_type": "str"
    },
    "current_year": {
        "description": "Returns the current year as an integer.",
        "module": "agent.tools.time_utils",
        "function": "current_year",
        "args": {},
        "return_type": "int"
    },
    "current_time": {
        "description": "Returns the current time as a formatted string.",
        "module": "agent.tools.time_utils",
        "function": "current_time",
        "args": {
            "format_24": "bool"
        },
        "return_type": "str"
    },
    "timestamp": {
        "description": "Returns the current timestamp as an integer.",
        "module": "agent.tools.time_utils",
        "function": "timestamp",
        "args": {},
        "return_type": "int"
    },
    "current_timezone": {
        "description": "Returns the current timezone as a string.",
        "module": "agent.tools.time_utils",
        "function": "current_timezone",
        "args": {},
        "return_type": "str"
    },
    "seconds_between": {
        "description": "Returns how many seconds are there between two datetime objects.",
        "module": "agent.tools.time_utils",
        "function": "seconds_between",
        "args": {
            "start": "datetime", 
            "end": "datetime"
        },
        "return_type": "int"
    },
    "add_seconds": {
        "description": "Add a number of seconds to a given datetime.",
        "module": "agent.tools.time_utils",
        "function": "add_seconds",
        "args": {
            "start": "datetime", 
            "seconds": "int"
        },
        "return_type": "datetime"
    },
    "subtract_seconds": {
        "description": "Subtract a number of seconds from a given datetime.",
        "module": "agent.tools.time_utils",
        "function": "subtract_seconds",
        "args": {
            "start": "datetime", 
            "seconds": "int"
        },
        "return_type": "datetime"
    },

    "factorial": {
        "description": "Returns the factorial of a non-negative integer n.",
        "module": "agent.tools.math_utils",
        "function": "factorial",
        "args": {
            "n": "int"
        },
        "return_type": "int"
    },
    "is_prime": {
        "description": "Returns True if n is prime, False otherwise.",
        "module": "agent.tools.math_utils",
        "function": "is_prime",
        "args": {
            "n": "int"
        },
        "return_type": "bool"
    },
    "logarithm": {
        "description": "Returns the logarithm of a value with the specified base.",
        "module": "agent.tools.math_utils",
        "function": "logarithm",
        "args": {
            "value": "float", "base": "float"
        },
        "return_type": "float"
    },
    "sqrt": {
        "description": "Returns the square root of a non-negative value.",
        "module": "agent.tools.math_utils",
        "function": "sqrt",
        "args": {
            "value": "float"
        },
        "return_type": "float"
    },
    "power": {
        "description": "Returns the result of raising base to the exponent power.",
        "module": "agent.tools.math_utils",
        "function": "power",
        "args": {
            "base": "float", 
            "exponent": "float"
        },
        "return_type": "float"
    },
    "add": {
        "description": "Returns the sum of two numbers.",
        "module": "agent.tools.math_utils",
        "function": "add",
        "args": {
            "a": "float", 
            "b": "float"
        },
        "return_type": "float"
    },
    "subtract": {
        "description": "Returns the difference of two numbers.",
        "module": "agent.tools.math_utils",
        "function": "subtract",
        "args": {
            "a": "float", 
            "b": "float"
        },
        "return_type": "float"
    },
    "multiply": {
        "description": "Returns the product of two numbers.",
        "module": "agent.tools.math_utils",
        "function": "multiply",
        "args": {
            "a": "float", 
            "b": "float"
        },
        "return_type": "float"
    },
    "divide": {
        "description": "Returns the quotient of two numbers. Returns -1 if division by zero",
        "module": "agent.tools.math_utils",
        "function": "divide",
        "args": {
            "a": "float", 
            "b": "float"
        },
        "return_type": "float"
    },
    "sine": {
        "description": "Returns the sine of an angle in radians.",
        "module": "agent.tools.math_utils",
        "function": "sine",
        "args": {
            "angle_rad": "float"
        },
        "return_type": "float"
    },
    "cosine": {
        "description": "Returns the cosine of an angle in radians.",
        "module": "agent.tools.math_utils",
        "function": "cosine",
        "args": {
            "angle_rad": "float"
        },
        "return_type": "float"
    },
    "tangent": {
        "description": "Returns the tangent of an angle in radians.",
        "module": "agent.tools.math_utils",
        "function": "tangent",
        "args": {
            "angle_rad": "float"
        },
        "return_type": "float"
    },
    
    "remember": {
        "description": "Stores a value with the associated key.",
        "module": "agent.tools.memory_store",
        "function": "remember",
        "args": {
            "key": "str", 
            "value": "any"
        },
        "return_type": "None"
    },
    "recall": {
        "description": "Retrieves the value associated with the given key.",
        "module": "agent.tools.memory_store",
        "function": "recall",
        "args": {
            "key": "str"
        },
        "return_type": "any"
    },
    "forget": {
        "description": "Removes the value associated with the given key.",
        "module": "agent.tools.memory_store",
        "function": "forget",
        "args": {
            "key": "str"
        },
        "return_type": "None"
    },
    "list_memory": {
        "description": "Lists all key-value pairs stored in memory.",
        "module": "agent.tools.memory_store",
        "function": "list_memory",
        "args": {},
        "return_type": "dict"
    },
    "clear_memory": {
        "description": "Clears all entries from the memory store.",
        "module": "agent.tools.memory_store",
        "function": "clear_memory",
        "args": {},
        "return_type": "None"
    },
    
    "system_status": {
        "description": "Returns the operating system, hostname, and current user.",
        "module": "agent.tools.system_info",
        "function": "system_status",
        "args": {},
        "return_type": "dict"
    },
    
    "add_task": {
        "description": "Adds a new task to the task list.",
        "module": "agent.tools.task_manager",
        "function": "add_task",
        "args": {
            "task": "str"
        },
        "return_type": "None"
    },
    "list_tasks": {
        "description": "Lists all tasks in the task list.",
        "module": "agent.tools.task_manager",
        "function": "list_tasks",
        "args": {},
        "return_type": "list"
    },
    "remove_task": {
        "description": "Removes a task from the task list by its index.",
        "module": "agent.tools.task_manager",
        "function": "remove_task",
        "args": {
            "index": "int"
        },
        "return_type": "None"
    },
    "clear_tasks": {
        "description": "Clears all tasks from the task list.",
        "module": "agent.tools.task_manager",
        "function": "clear_tasks",
        "args": {},
        "return_type": "None"
    },

    "word_count": {
        "description": "Returns the number of words in the given text.",
        "module": "agent.tools.text_utils",
        "function": "word_count",
        "args": {
            "text": "str"
        },
        "return_type": "int"
    },
    "summarize_length": {
        "description": "Returns a summary of the text length including character and word counts.",
        "module": "agent.tools.text_utils",
        "function": "summarize_length",
        "args": {
            "text": "str"
        },
        "return_type": "dict"
    },
    "reverse_text": {
        "description": "Reverses the given text string.",
        "module": "agent.tools.text_utils",
        "function": "reverse_text",
        "args": {
            "text": "str"
        },
        "return_type": "str"
    },

    "mm2cm": {
        "description": "Convert millimeters to centimeters.",
        "module": "agent.tools.unit_converter",
        "function": "mm2cm",
        "args": {
            "mm": "float"
        },
        "return_type": "float"
    },
    "cm2mm": {
        "description": "Convert centimeters to millimeters.",
        "module": "agent.tools.unit_converter",
        "function": "cm2mm",
        "args": {
            "cm": "float"
        },
        "return_type": "float"
    },
    "inches2cm": {
        "description": "Convert inches to centimeters.",
        "module": "agent.tools.unit_converter",
        "function": "inches2cm",
        "args": {
            "inches": "float"
        },
        "return_type": "float"
    },
    "cm2inches": {
        "description": "Convert centimeters to inches.",
        "module": "agent.tools.unit_converter",
        "function": "cm2inches",
        "args": {
            "cm": "float"
        },
        "return_type": "float"
    },
    "pounds2kg": {
        "description": "Convert pounds to kilograms.",
        "module": "agent.tools.unit_converter",
        "function": "pounds2kg",
        "args": {
            "pounds": "float"
        },
        "return_type": "float"
    },
    "kg2pounds": {
        "description": "Convert kilograms to pounds.",
        "module": "agent.tools.unit_converter",
        "function": "kg2pounds",
        "args": {
            "kg": "float"
        },
        "return_type": "float"
    },
    "fahrenheit2celsius": {
        "description": "Convert Fahrenheit to Celsius.",
        "module": "agent.tools.unit_converter",
        "function": "fahrenheit2celsius",
        "args": {
            "fahrenheit": "float"
        },
        "return_type": "float"
    },
    "celsius2fahrenheit": {
        "description": "Convert Celsius to Fahrenheit.",
        "module": "agent.tools.unit_converter",
        "function": "celsius2fahrenheit",
        "args": {
            "celsius": "float"
        },
        "return_type": "float"
    },
    "liters2gallons": {
        "description": "Convert liters to gallons.",
        "module": "agent.tools.unit_converter",
        "function": "liters2gallons",
        "args": {
            "liters": "float"
        },
        "return_type": "float"
    },
    "gallons2liters": {
        "description": "Convert gallons to liters.",
        "module": "agent.tools.unit_converter",
        "function": "gallons2liters",
        "args": {
            "gallons": "float"
        },
        "return_type": "float"
    },
    "radians2degrees": {
        "description": "Convert radians to degrees.",
        "module": "agent.tools.unit_converter",
        "function": "radians2degrees",
        "args": {
            "radians": "float"
        },
        "return_type": "float"
    },
    "degrees2radians": {
        "description": "Convert degrees to radians.",
        "module": "agent.tools.unit_converter",
        "function": "degrees2radians",
        "args": {
            "degrees": "float"
        },
        "return_type": "float"
    },
}

def tools_for_prompt():
    lines = []
    for name, meta in TOOLS.items():
        args = ", ".join(meta["args"].keys())
        lines.append(f"- {name}({args}): {meta['description']}")
    return "\n".join(lines)

print(tools_for_prompt())