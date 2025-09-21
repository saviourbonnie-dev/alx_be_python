# daily_reminder.py

# Step 1: Prompt the user for details
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Step 2: Match Case for priority handling
match priority:
    case "high":
        priority_text = "high"
    case "medium":
        priority_text = "medium"
    case "low":
        priority_text = "low"
    case _:
        priority_text = "unspecified"

# Step 3: Conditional output based on time sensitivity
if time_bound == "yes":
    print(f"Reminder: '{task}' is a {priority_text} priority task that requires immediate attention today!")
else:
    print(f"Note: '{task}' is a {priority_text} priority task. Consider completing it when you have free time.")

