def f(x, a, b, c):
    return {a: b, b: c, c: a}[x]


print(f(3, a=3, b=4, c=5), 4)
print(f(5, a=3, b=4, c=5), 3)
