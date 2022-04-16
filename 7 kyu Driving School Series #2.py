def cost(mins):
    return 10 * ((mins + 54) // 30)


print(cost(45), 30)
print(cost(63), 30)
print(cost(84), 40)
print(cost(102), 50)
print(cost(273), 100)
