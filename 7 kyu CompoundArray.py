def compound_array(a, b):
    lst = []

    while a or b:
        lst += a[:1] + b[:1]
        a = a[1:]
        b = b[1:]

    return lst


print(compound_array([1, 2, 3, 4, 5, 6], [9, 8, 7, 6]), [1, 9, 2, 8, 3, 7, 4, 6, 5, 6])
print(compound_array([0, 1, 2], [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]), [0, 9, 1, 8, 2, 7, 6, 5, 4, 3, 2, 1, 0])
