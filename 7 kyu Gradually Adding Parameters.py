def add(*args):
    return sum(i * j for i, j in enumerate(args, 1))


print(add(), 0, 'No arguments should return 0')
print(add(100, 200, 300), 1400)
print(add(2), 2)
