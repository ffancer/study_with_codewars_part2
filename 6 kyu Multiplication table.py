def multiplication_table(size):
    lst = []

    for i in range(1, size ** 2 + 1):
        lst.append(i)

    return lst

print(multiplication_table(3), [[1, 2, 3], [2, 4, 6], [3, 6, 9]])
