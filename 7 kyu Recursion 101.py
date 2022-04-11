def solve(a, b):
    while a == 0 or b == 0:
        if a >= 2 * b:
            a = a - 2 * b
        if b >= 2 * a:
            b = b - 2 * a
    return [a, b]


print(solve(6, 19), [6, 7])
print(solve(2, 1), [0, 1])
print(solve(22, 5), [0, 1])
print(solve(2, 10), [2, 2])
print(solve(0, 10), [0, 10])
