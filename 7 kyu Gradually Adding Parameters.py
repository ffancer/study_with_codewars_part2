def add(*args):
    for i,j in enumerate(args, 1):
        print(i, j)


print(add(), 0, 'No arguments should return 0')
print(add(100, 200, 300), 1400)
print(add(2), 2)
