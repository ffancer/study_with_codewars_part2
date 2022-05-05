def sum_diagonals(matrix):
    # first diagonal
    first_dgnl = sum(matrix[i][i] for i in range(len(matrix)))

    # second diagonal
    second_dgnl = sum(matrix[len(matrix) - i - 1][len(matrix) - i - 1] for i in range(len(matrix)))

    return first_dgnl + second_dgnl


print(sum_diagonals([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), 1 + 5 + 9 + 3 + 5 + 7)
print(sum_diagonals([]))
