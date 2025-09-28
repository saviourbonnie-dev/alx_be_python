from datetime import datetime, timedelta

# Part 1: Display the current date and time
def display_current_datetime():
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print("Current date and time:", formatted_date)

# Part 2: Calculate a future date
def calculate_future_date(days):
    today = datetime.now().date()
    future_date = today + timedelta(days=days)
    print("Future date:", future_date.strftime("%Y-%m-%d"))

def main():
    # Show current date and time
    display_current_datetime()

    # Ask the user for number of days
    days = int(input("Enter the number of days to add to the current date: "))

    # Show the future date
    calculate_future_date(days)

if __name__ == "__main__":
    main()
