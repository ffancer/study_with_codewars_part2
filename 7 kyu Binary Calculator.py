def calculate(n1, n2, o):
    return {
        'add': bin(int(n1) + int(n2))[2:],
        'subtract': bin(int(n1) - int(n2))[2:],
        'multiply': bin(int(n1) * int(n2))[2:]
    }[o]


print(calculate('1', '1', 'add'), '10')
print(calculate('1', '1', 'subtract'), '0')
print(calculate('1', '1', 'multiply'), '1')
