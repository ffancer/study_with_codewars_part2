def square(number):
    total = 1
    for i in range(number):

        temp = i * 2
        total += temp

    return total

print(square(1), 1)
print(square(3), 4)
print(square(4), 8)
print(square(16), 32768)
print(square(32), 2147483648)
