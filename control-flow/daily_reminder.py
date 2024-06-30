task = input("Enter your task:")
priority = input("Priority (high/medium/low):")
time_bound =input("Is it time-bound? (yes/no):")

match priority:
    case "high":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
        else:
            print(f"Reminder: '{task}' is a high priority task. Try to complete it soon.")
    case "medium":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a medium priority task that needs to be done today.")
        else:
            print(f"Reminder: '{task}' is a medium priority task. Plan to complete it in the near future.")
    case "low":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a low priority task but it needs to be done today.")
        else:
            print(f"Reminder: '{task}' is a low priority task. Consider completing it when you have free time.")
