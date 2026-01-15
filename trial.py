from datetime import date
from tools import date_calculator, math_utils, memory_store, system_info, task_manager, text_utils, time_utils

__all__ = [
    "date_calculator",
    "math_utils",
    "memory_store",
    "system_info",
    "task_manager",
    "text_utils",
    "time_utils",
]

print("Tools module loaded with: ", __all__)
print("=====================================================================")
print("Testing date utils module: ")
startDate = date(2026, 1, 15)
endDate = date(2026, 2, 15)
addDays = 12
subDays = 5
print("Validation: start[", date_calculator.is_valid_date("2026-02-30"),"], end[",  date_calculator.is_valid_date("2026-02-28"), "]")
print("Days between ", startDate, " and ", endDate, ": ", date_calculator.days_between(startDate, endDate))
print("Days until ", endDate, ": ", date_calculator.days_until(endDate))
print("Adding ", addDays, " days to ", startDate, ": ", date_calculator.add_days(startDate, addDays))
print("Subtracting ", subDays, " days from ", endDate, ": ", date_calculator.subtract_days(endDate, subDays))
print("=====================================================================")
print("Testing math utils module: ")
print("5 + 3 = ", math_utils.add(5, 3))
print("5 - 3 = ", math_utils.subtract(5, 3))
print("5 * 3 = ", math_utils.multiply(5, 3))
print("5 / 0 = ", math_utils.divide(5, 0))
print("5 / 2 = ", math_utils.divide(5, 2))
print("2 ^ 3 = ", math_utils.power(2, 3))
print("sqrt(16) = ", math_utils.sqrt(16))
print("5! = ", math_utils.factorial(5))
print("log10(100) = ", math_utils.logarithm(100))
print("sin(π/2) = ", math_utils.sine(math_utils.radians(90)))
print("Is 23 prime? ", math_utils.is_prime(23))
print("=====================================================================")
print("Testing text utils module: ")
sample_text = "Hello world! This is a test."
print("Word count: ", text_utils.word_count(sample_text))
print("Summary: ", text_utils.summarize_length(sample_text))
print("Reversed text: ", text_utils.reverse_text(sample_text))
print("=====================================================================")
print("Testing time utils module: ")
print("Current datetime: ", time_utils.current_datetime())
print("Current date: ", time_utils.current_date())
print("Current time (24h): ", time_utils.current_time(format_24=True))
print("Current time (12h): ", time_utils.current_time(format_24=False))
print("Current timestamp: ", time_utils.timestamp())
print("Current timezone: ", time_utils.current_timezone())
print("=====================================================================")
