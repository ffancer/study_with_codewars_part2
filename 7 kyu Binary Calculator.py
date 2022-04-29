def calculate(n1, n2, o):
    ops = {'add': lambda x, y: x + y, 'subtract': lambda x, y: x - y, 'multiply': lambda x, y: x * y}
    return "{0:b}".format(ops[o](int(n1, 2), int(n2, 2)))


print(calculate('1', '1', 'add'), '10')
print(calculate('1', '1', 'subtract'), '0')
print(calculate('1', '1', 'multiply'), '1')
print(calculate('10101101', '1011011101', 'multiply'), '11110111101011001')
