def pattern(n):
    s = ''

    for i in range(1, n, 2):
        s += str(i) * i + '\n'

    return s

print(pattern(4), "1\n333")
# print(pattern(1), "1")
# print(pattern(5), "1\n333\n55555")
# print(pattern(5), "1\n333\n55555")
# print(pattern(0), "")
# print(pattern(-25), "")
