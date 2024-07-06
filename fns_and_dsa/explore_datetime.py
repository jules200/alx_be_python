from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    current_date_formatted = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {current_date_formatted}")
    
    dd = int(input("Enter the number of days to add to the current date: "))
    calculate_future_date = (current_date + timedelta(days=dd)).date()
    future_date_formatted = future_date.strftime("%Y-%m-%d")
    
    print(f"Future date: {future_date_formatted}")

display_current_datetime()