def add(*args):
    return round(sum(j / (i + 1) for i, j in enumerate(args)))


print(add(), 0, 'No arguments should return 0')
print(add(100, 200, 300), 300)
print(add(2), 2)
print(add(4, -3, -2), 2)
print(add(-1, -2, -3, -4), -4)
