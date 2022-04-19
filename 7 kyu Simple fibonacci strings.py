def solve(n):
    ans = ''

    for i in range(0, n+1):
        ans += bin(i)[2:]

    return ans


print(solve(0), '0')
print(solve(1), '01')
print(solve(2), '010')
print(solve(3), '01001')
print(solve(5), '0100101001001')
