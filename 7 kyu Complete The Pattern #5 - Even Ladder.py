def pattern(n):
    return '\n'.join(i * str(i) for i in range(2, n + 1, 2))


print(pattern(2), "22")
print(pattern(1), "")
print(pattern(5), "22\n4444")
print(pattern(6), "22\n4444\n666666")
print(pattern(0), "")
print(pattern(-25), "")
