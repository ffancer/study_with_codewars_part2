def f(x, a, b, c):
    a, b, c = b, c, a
    return a, b, c

print(f(3, a=3, b=4, c=5), 4)
print(f(5, a=3, b=4, c=5), 3)
