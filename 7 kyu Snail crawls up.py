from math import ceil


def snail(column, day, night):
    return 1 if day >= column else ceil((column - day) / (day - night)) + 1


print(snail(3, 2, 1), 2)
print(snail(10, 3, 1), 5)
print(snail(10, 3, 2), 8)
print(snail(100, 20, 5), 7)
print(snail(5, 10, 3), 1)
