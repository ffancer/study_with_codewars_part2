def sum_diagonals(matrix):
    matrix_len = len(matrix[0])

    m1 = [matrix[x][x] for x in range(matrix_len)]
    m2 = [matrix[x][-x - 1] for x in range(matrix_len)]

    return sum(m1) + sum(m2)


print(sum_diagonals([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), 1 + 5 + 9 + 3 + 5 + 7)
print(sum_diagonals([]))
print(sum_diagonals([4]))
print(sum_diagonals([[4], [4]]))
