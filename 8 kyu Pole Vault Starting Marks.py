first = (10.67 - 9.45) / (1.83 - 1.52)
second = 9.45 - first * 1.52


def starting_mark(height):
    return round(first * height + second, 2)


print(starting_mark(1.52), 9.45)
print(starting_mark(1.83), 10.67)
print(starting_mark(1.22), 8.27)
print(starting_mark(2.13), 11.85)
print(starting_mark(1.75), 10.36)
