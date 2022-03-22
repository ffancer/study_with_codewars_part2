def calculate(a, o, b):
    result = None

    if o == "+":
        result = a + b
    if o == "-":
        result = a - b
    if o == "/" and b != 0:
        result = a / b
    if o == "*":
        result = a * b
    return result


print(calculate(6, "-", 1.5), 4.5)
print(calculate(-4, "*", 8), -32)
print(calculate(49, "/", -7), -7)
print(calculate(8, "m", 2), None)
print(calculate(4, "/", 0), None)
