def minimum(a, x):
    i = 1
    while a % x != 0:
        a += i
        # i += 1
    return a - i


print(minimum(1, 1), 0)
print(minimum(9, 4), 1)
print(minimum(10, 6), 2)
print(minimum(60, 45), 15)
print(minimum(57, 50), 7)
print(minimum(28, 16), 4)
print(minimum(84, 80), 4)
print(minimum(129, 49), 18)
print(minimum(150, 67), 16)
print(minimum(121, 46), 17)
print(minimum(83, 81), 2)
print(minimum(89, 74), 15)
