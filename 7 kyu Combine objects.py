def combine(*args):
    dct = {}

    for b in args:
        for i, j in b.items():
            dct[i] = j + dct.get(i, 0)

    return dct


objA = {'a': 10, 'b': 20, 'c': 30}
objB = {'a': 3, 'c': 6, 'd': 3}
objC = {'a': 5, 'd': 11, 'e': 8}
objD = {'c': 3}

print(combine(objA, objB), {'a': 13, 'b': 20, 'c': 36, 'd': 3})
print(combine(objA, objC), {'a': 15, 'b': 20, 'c': 30, 'd': 11, 'e': 8})
print(combine(objA, objB, objC), {'a': 18, 'b': 20, 'c': 36, 'd': 14, 'e': 8})
print(combine(objA, objC, objD), {'a': 15, 'b': 20, 'c': 33, 'd': 11, 'e': 8})
print(combine({}, {}, {}), {})
print(combine(objA, objC, {}), {'a': 15, 'b': 20, 'c': 30, 'd': 11, 'e': 8})
