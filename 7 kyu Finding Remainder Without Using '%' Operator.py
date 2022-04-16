def remainder(dividend, divisor):
    return dividend - (dividend // divisor) * divisor


print(remainder(3, 2), 1)
print(remainder(19, 2), 1)
print(remainder(10, 2), 0)
print(remainder(34, 7), 6)
print(remainder(27, 5), 2)
