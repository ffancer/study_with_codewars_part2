def pattern(n):
    s = ""

    if n == 0 or not n:
        return ""

    for i in range(1, n + 1):
        if i != 1:
            s += '\n'
        for j in range(i, n + 1):
            s += str(j)
        for j in range(1, i):
            s += str(j)

    return s


print(pattern(7), "1234567\n2345671\n3456712\n4567123\n5671234\n6712345\n7123456")
print(pattern(1), "1")
print(pattern(4), "1234\n2341\n3412\n4123")
print(pattern(0), "")
print(pattern(-25), "")
