def sum_diagonals(matrix):
    total = 0

    for i, j in enumerate(matrix):
        total += j[i]

    total += sum(matrix[len(matrix) - i - 1][len(matrix)- i - 1] for i in range(len(matrix)))

    return total


print(sum_diagonals([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), 1 + 5 + 9 + 3 + 5 + 7)
print(sum_diagonals([]))
