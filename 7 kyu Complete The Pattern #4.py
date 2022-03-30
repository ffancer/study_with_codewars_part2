def pattern(n):
    ans = ''

    for i in range(1, n+1):
        ans += str(i) + '\n'

    return ans


print(pattern(1), "1")
print(pattern(2), "12\n2")
print(pattern(5), "12345\n2345\n345\n45\n5")
print(pattern(0), "")
print(pattern(-25), "")
