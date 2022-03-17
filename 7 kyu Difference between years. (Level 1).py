def how_many_years(date1, date2):
    return int(date1.split('/')[0])


print(how_many_years('1997/10/10', '2015/10/10'), 18)
print(how_many_years('1990/10/10', '2015/10/10'), 25)
print(how_many_years('2015/10/10', '1990/10/10'), 25)
print(how_many_years('1992/10/24', '2015/10/24'), 23)
print(how_many_years('2018/10/10', '2000/10/10'), 18)
