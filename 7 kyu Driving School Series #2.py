from math import floor
def cost(mins):
    a = 0 if mins % 30 <= 5 else 1
    total = floor(mins / 30) + a
    return total


print(cost(45), 30)
print(cost(63), 30)
print(cost(84), 40)
print(cost(102), 50)
print(cost(273), 100)
