task = input("Enter your task:")
priority = input("Priority (high/medium/low):").upper()
time_bound = input("Is it time-bound? (yes/no):")

match priority :
    case "HIGH" :
        if time_bound == "yes" :
            print(f"Reminder: '{task}' is a {priority} priority task that requires immediate attention today!")
        else :
            print(f"Note: '{task}' is a {priority} priority task. Consider completing it when you have free time.")
    case "MEDIUM" :
        if time_bound == "yes" :
            print(f"Reminder: '{task}' is a {priority} priority task that requires immediate attention today!")
        else :
            print(f"Note: '{task}' is a {priority} priority task. Consider completing it when you have free time.")
    case "LOW" :
        if time_bound == "yes" :
            print(f"Reminder: '{task}' is a {priority} priority task that requires immediate attention today!")
        else :
            print(f"Note: '{task}' is a {priority} priority task. Consider completing it when you have free time.")
    case _ :
        if time_bound == "yes" :
            print(f"Reminder: '{task}' is a No priority task that requires immediate attention today!")
        else :
            print(f"Note: '{task}' is a No priority task. Consider completing it when you have free time.")
    