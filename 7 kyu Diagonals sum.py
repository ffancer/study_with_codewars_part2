def sum_diagonals(matrix):
    total = 0
    for i, j in enumerate(matrix):
        total += j[i]
    return total

print(sum_diagonals([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), 1 + 5 + 9 + 3 + 5 + 7)
