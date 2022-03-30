def pattern(n, x = ''):
    if n <= 0:
        return ''

    x = str(n) + x
    return x if n == 1 else pattern(n-1, x) + '\n' + x


print(pattern(1), "1")
print(pattern(2), "12\n2")
print(pattern(5), "12345\n2345\n345\n45\n5")
print(pattern(0), "")
print(pattern(-25), "")
