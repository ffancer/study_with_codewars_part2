from math import log


def powerof4(n):
    return log(n) / log(4) % 1 == 0 if type(n) is int and n > 0 else False


print(powerof4(4), True, "Wrong result for 4")
print(powerof4(40), False, "Wrong result for 40")
print(powerof4(1), True, "Wrong result for 1")
