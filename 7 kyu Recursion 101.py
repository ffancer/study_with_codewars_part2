def solve(a, b):
    if a == 0 or b == 0:
        return [a, b]
    elif a >= (2 * b):
        return solve((a - 2 * b), b)
    elif b >= (2 * a):
        return solve(a, (b - 2 * a))
    return [a, b]


print(solve(6, 19), [6, 7])
print(solve(2, 1), [0, 1])
print(solve(22, 5), [0, 1])
print(solve(2, 10), [2, 2])
print(solve(0, 10), [0, 10])
