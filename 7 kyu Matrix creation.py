import numpy as np


def get_matrix(n):
    if n == 0:
        return []
    else:
        zerom = np.zeros(((n, n)), dtype = int)
        for i in range(n):
            for j in range(n):
                if i == j:
                    zerom[i][j] += 1
        return zerom.tolist()


print(get_matrix(0), [])
print(get_matrix(1), [[1]])
print(get_matrix(2), [[1, 0], [0, 1]])
print(get_matrix(3), [[1, 0, 0], [0, 1, 0], [0, 0, 1]])
print(get_matrix(5), [[1, 0, 0, 0, 0], [0, 1, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 1, 0], [0, 0, 0, 0, 1]])