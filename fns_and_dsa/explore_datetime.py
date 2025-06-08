import datetime


def display_current_datetime() :
    current_date = datetime.datetime.now()
    print("Current date and time:", current_date.strftime("%Y-%m-%d %H:%M:%S"))


def calculate_future_date(days) :
    current_date = datetime.datetime.now()
    future_date = current_date + datetime.timedelta(days=days)

    print(f"Future date: ",future_date.strftime("%Y-%m-%d"))

display_current_datetime()
days = int(input("Enter the number of days to add to the current date: "))
calculate_future_date(days)