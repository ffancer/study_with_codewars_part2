def f(x, a, b, c):
    if x == a:
        return b
    elif x == b:
        return c
    elif x == c:
        return a


print(f(3, a=3, b=4, c=5), 4)
print(f(5, a=3, b=4, c=5), 3)
