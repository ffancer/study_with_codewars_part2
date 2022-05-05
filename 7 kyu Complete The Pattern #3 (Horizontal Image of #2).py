def pattern(n):
    s = ""
    i = 1

    while i <= n:
        if len(s) != 0:
            s = s + "\n"
        j = 0
        while j < i:
            s = s + str(n - j)
            j = j + 1
        i = i + 1

    return s


print(pattern(1), "1")
print(pattern(2), "2\n21")
print(pattern(5), "5\n54\n543\n5432\n54321")
print(pattern(0), "")
print(pattern(-25), "")
