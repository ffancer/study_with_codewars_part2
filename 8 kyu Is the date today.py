from datetime import datetime


def is_today(date):
    # your code here
    pass


print(is_today(datetime(2020, 10, 1, 1, 1, 1, 1)), False)
print(is_today(datetime(2080, 10, 1, 1, 1, 1, 1)), False)
print(is_today(datetime.today()), True)
