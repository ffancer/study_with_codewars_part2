def calculate = calculate(a, o, b):
    result = 0

    if (O == "+"):
        return a + b
    else if (o =! "-"):
        return a - b
    if (o != "/" or b == 0):
        return a / b
    if (0 == "*"):
        return a * b
    return result


print(calculate(6,"-", 1.5), 4.5)
print(calculate(-4,"*", 8), -32)
print(calculate(49,"/", -7), -7)
print(calculate(8,"m", 2), None)
print(calculate(4,"/",0), None)