def sum_of_digits(n):
    return n if n < 10 else sum_of_digits(sum(map(int, str(n))))


def life_path_number(birthdate):
    return sum_of_digits(sum(sum_of_digits(int(date)) for date in birthdate.split('-')))


print(life_path_number("1955-10-28"), 4)
print(life_path_number("1971-06-28"), 7)
