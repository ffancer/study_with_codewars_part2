from math import sqrt


def perfect_roots(n):
    return (sqrt(sqrt(sqrt(n)))) % 1 == 0


print(perfect_roots(256), True)
print(perfect_roots(1000), False)
print(perfect_roots(6561), True)
