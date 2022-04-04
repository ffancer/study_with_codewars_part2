def geometric_sequence_elements(a, r, n):
    lst = [a]

    for i in range(n-1):
        lst.append(lst[-1] * r)

    return ', '.join(str(i) for i in lst)


print(geometric_sequence_elements(2, 3, 5), '2, 6, 18, 54, 162')
print(geometric_sequence_elements(2, 2, 10), '2, 4, 8, 16, 32, 64, 128, 256, 512, 1024')
print(geometric_sequence_elements(1, -2, 10), '1, -2, 4, -8, 16, -32, 64, -128, 256, -512')
