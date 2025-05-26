task = input("Enter your task: ")
time_bound = input("Is it time-bound? (yes/no): ")
priority = input("Priority (high/medium/low): ").lower()

# Match Case to handle priority
match priority:
    case "high":
        message = f"Reminder: Your task '{task}' is HIGH priority."
    case "medium":
        message = f"Reminder: Your task '{task}' is of MEDIUM priority."
    case "low":
        message = f"Reminder: Your task '{task}' is LOW priority."
    case _:
        message = f"Reminder: Your task '{task}' has an UNKNOWN priority."

# Time-sensitive check
if time_bound == "yes":
    message += " This is a time-sensitive task that requires immediate attention today!"

# Print reminder
print(message)