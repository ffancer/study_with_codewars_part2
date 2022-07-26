from datetime import datetime


def is_today(date):
    return str(datetime.today()).split('-')[2].split()[0] == date


print(is_today(datetime(2020, 10, 1, 1, 1, 1, 1)), False)
print(is_today(datetime(2080, 10, 1, 1, 1, 1, 1)), False)
print(is_today(datetime.today()), True)
