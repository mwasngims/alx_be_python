# daily_reminder.py

def main():
    # Prompt for task details
    task = input("Enter your task for today: ")
    priority = input("Enter the priority level (high, medium, low): ").lower()
    time_bound = input("Is the task time-bound (yes or no)?: ").lower()

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

    # If the task is time-bound, emphasize urgency
    if time_bound == "yes":
        message += " This is a time-sensitive task that requires immediate attention today!"

    # Print the reminder 3 times using a loop
    count = 0
    while count < 1:
        print(message)
        count += 1

if __name__ == "__main__":
    main()
