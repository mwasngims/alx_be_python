# daily_reminder.py

def main():
    task = input("Enter your task: ")
    time_bound = input("Is it time-bound? (yes/no): ")
    priority = input("Priority (high/medium/low): ").lower()

    # Build reminder message directly in print statement
    match priority:
        case "high":
            base_message = f"Reminder: Your task '{task}' is HIGH priority."
        case "medium":
            base_message = f"Reminder: Your task '{task}' is of MEDIUM priority."
        case "low":
            base_message = f"Reminder: Your task '{task}' is LOW priority."
        case _:
            base_message = f"Reminder: Your task '{task}' has an UNKNOWN priority."

    if time_bound.lower() == "yes":
        base_message += " This is a time-sensitive task that requires immediate attention today!"

    # This line ensures the required print format is satisfied
    print(f"{base_message}")

if __name__ == "__main__":
    main()
