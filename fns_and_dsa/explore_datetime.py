from datetime import datetime
import datetime
def display_current_datetime():
    current_date = datetime.datetime.now()
    print(current_date)
    dd = int(input("Enter the number of days to add to the current date: "))
    calculate_future_date = current_date.date() + datetime.timedelta(days=dd)
    print(f"Future date: {calculate_future_date}")
    

display_current_datetime()