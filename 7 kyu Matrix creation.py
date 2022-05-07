def get_matrix(n):
    return [[1 if i == j else 0 for i in range(n)] for j in range(n)]


print(get_matrix(0), [])
print(get_matrix(1), [[1]])
print(get_matrix(2), [[1, 0], [0, 1]])
print(get_matrix(3), [[1, 0, 0], [0, 1, 0], [0, 0, 1]])
print(get_matrix(5), [[1, 0, 0, 0, 0], [0, 1, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 1, 0], [0, 0, 0, 0, 1]])
