def strange_math(n, k):
    return sorted(str(i) for i in range(0, n + 1)).index(str(k))


print(strange_math(11, 2), 4, 'Wrong result for (11,2)')
print(strange_math(15, 5), 11, 'Wrong result for (15,5)')
print(strange_math(15, 15), 7, 'Wrong result for (15,15)')
