def sum_diagonals(matrix):
    if len(matrix) == 1:
        return matrix[0] * 2

    # first diagonal
    first_dgnl = sum(matrix[i][i] for i in range(len(matrix)))

    # second diagonal
    second_dgnl = sum(matrix[i][len(matrix) - i - 1] for i in range(len(matrix)))

    return first_dgnl + second_dgnl


print(sum_diagonals([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), 1 + 5 + 9 + 3 + 5 + 7)
print(sum_diagonals([]))
