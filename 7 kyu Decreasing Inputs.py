def add(*args):
    total = 0
    for i, j in enumerate(args):
        total += j / (i + 1)
    return round(total)


print(add(), 0, 'No arguments should return 0')
print(add(100, 200, 300), 300)
print(add(2), 2)
print(add(4, -3, -2), 2)
print(add(-1, -2, -3, -4), -4)
