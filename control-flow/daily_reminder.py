task = input("Enter your task: ")
time_bound = input("Is it time-bound? (yes/no): ")
priority = input("Priority (high/medium/low): ").lower()

# Match Case to handle priority
match priority:
    case "high":
        message = f"Note: '{task}' is a high priority task. Consider completing it when you have free time."
    case "medium":
        message = f"Note: '{task}' is a medium priority task. Consider completing it when you have free time.."
    case "low":
        message = f"Note: '{task}' is a low priority task. Consider completing it when you have free time."
    case _:
        message = f"Note: '{task}' is a low priority task. Consider completing it when you have free time."

# Time-sensitive check
if time_bound == "yes":
    message = f"Reminder: '{task}' is a {priority} priority task that requires immediate attention today!"

# Print reminder
print(message)