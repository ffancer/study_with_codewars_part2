from datetime import datetime
from datetime import timedelta

def date_nb_days(a0, a, p):
    day = 0
    start = '2016/01/01'
    while a0 < a:
        a0 = a0 + (a0*p/100/360)
        day += 1
    date = datetime.strptime(start, '%Y/%m/%d')
    date += timedelta(days=day)
    return datetime.strftime(date, '%Y-%m-%d')


print(date_nb_days(4281, 5087, 2), "2024-07-03")
print(date_nb_days(4620, 5188, 2), "2021-09-19")
print(date_nb_days(9999, 11427, 6), "2018-03-13")
print(date_nb_days(3525, 4822, 3), "2026-04-18")
print(date_nb_days(5923, 6465, 6), "2017-06-10")
print(date_nb_days(4254, 4761, 8), "2017-05-22")
print(date_nb_days(1244, 2566, 4), "2033-11-04")
print(date_nb_days(6328, 7517, 5), "2019-05-25")
print(date_nb_days(2920, 3834, 2), "2029-06-03")
print(date_nb_days(7792, 8987, 4), "2019-07-09")
