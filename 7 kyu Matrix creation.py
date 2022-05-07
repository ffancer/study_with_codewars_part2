def get_matrix(n):
    lst = []

    for i in range(n):
        lst.append([0])

    return lst


print(get_matrix(0), [])
print(get_matrix(1), [[1]])
print(get_matrix(2), [[1, 0], [0, 1]])
print(get_matrix(3), [[1, 0, 0], [0, 1, 0], [0, 0, 1]])
print(get_matrix(5), [[1, 0, 0, 0, 0], [0, 1, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 1, 0], [0, 0, 0, 0, 1]])