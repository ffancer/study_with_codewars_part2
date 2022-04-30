def pattern(n):
    return '\n'.join(str(i) * i for i in range(1, n+1, 2))


print(pattern(4), "1\n333")
print(pattern(1), "1")
print(pattern(5), "1\n333\n55555")
print(pattern(5), "1\n333\n55555")
print(pattern(0), "")
print(pattern(-25), "")
