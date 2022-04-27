def sumin(n):
    total = 0

    for i in range(1, n):
        total += ((i * (n + 1 - i)) + (i * (n - i)))

    return total + n


def sumax(n):
    pass


def sumsum(n):
    pass


print(sumin(5), 55)
print(sumax(8), 372)
print(sumsum(8), 576)
print(sumin(15), 1240)
