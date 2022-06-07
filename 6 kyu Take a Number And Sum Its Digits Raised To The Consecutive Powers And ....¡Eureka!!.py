def sum_dig_pow(a, b):
    lst = []

    for i in range(a, b + 1):
        j = 0
        k = 1
        for c in str(i):
            j += int(c) ** k
            k += 1
        if j == i:
            lst.append(j)

    return lst


print(sum_dig_pow(1, 10), [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(sum_dig_pow(1, 100), [1, 2, 3, 4, 5, 6, 7, 8, 9, 89])
print(sum_dig_pow(10, 89), [89])
print(sum_dig_pow(10, 100), [89])
print(sum_dig_pow(90, 100), [])
print(sum_dig_pow(89, 135), [89, 135])
