def distinct_digit_year(year):
    year += 1

    while len(set(str(year))) != 4:
        year += 1

    return year


print(distinct_digit_year(1987), 2013)
print(distinct_digit_year(2013), 2014)
