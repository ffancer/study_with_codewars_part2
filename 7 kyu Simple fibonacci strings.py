def solve(n):
    i, j = '01'

    for k in range(n):
        i, j = i + j, i

    return i


print(solve(0), '0')
print(solve(1), '01')
print(solve(2), '010')
print(solve(3), '01001')
print(solve(5), '0100101001001')
