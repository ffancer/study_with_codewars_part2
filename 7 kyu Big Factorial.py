from math import factorial as fact


def factorial(n):
    return fact(n) if n >= 0 else None


print(factorial(1), 1)
print(factorial(4), 24)
print(factorial(5), 120)
