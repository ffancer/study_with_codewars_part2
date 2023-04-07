def number_to_pwr(number, p):
    total = 1

    for i in range(p):
        total *= number

    return total


print(number_to_pwr(4, 2), 16)
print(number_to_pwr(10, 4), 10000)
print(number_to_pwr(10, 0), 1)
