# 7 kyu
# Principal Diagonal | VS | Secondary Diagonal


def diagonal(matrix):
    principal_diagonal, secondary_diagonal = 0, 0

    for i in range(len(matrix)):
        principal_diagonal += matrix[i][i]
        secondary_diagonal += matrix[len(matrix) - 1 - i][i]

    return "Secondary Diagonal win!" if principal_diagonal < secondary_diagonal else "Principal Diagonal win!" \
        if principal_diagonal > secondary_diagonal else "Draw!"


print(diagonal([[2, 2, 2],
                [4, 2, 6],
                [8, 8, 2]]), "Secondary Diagonal win!")
print(diagonal([[2, 2, 2],
                [4, 2, 6],
                [1, 8, 2]]), "Principal Diagonal win!")
print(diagonal([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]]), "Draw!")
print(diagonal([[1, 2, 2, 5, 1],
                [4, 1, 6, 1, 1],
                [1, 8, 5, 6, 2],
                [1, 5, 2, 1, 2],
                [1, 8, 2, 6, 1]]), "Secondary Diagonal win!")
print(diagonal([[88, 2, 2, 5, 1, 1, 2, 2, 5, 1],
                [4, 1, 6, 1, 1, 1, 2, 2, 1, 1],
                [1, 8, 1, 6, 2, 1, 2, 1, 5, 1],
                [1, 5, 2, 1, 2, 1, 1, 2, 5, 1],
                [1, 8, 2, 6, 1, 1, 2, 2, 5, 1],
                [1, 2, 2, 5, 1, 1, 2, 2, 5, 1],
                [1, 2, 2, 1, 1, 1, 1, 2, 5, 1],
                [1, 2, 1, 5, 1, 1, 2, 1, 5, 1],
                [1, 1, 2, 5, 1, 1, 2, 2, 1, 1],
                [88, 2, 2, 5, 1, 1, 2, 2, 5, 1]]), "Draw!")
print(diagonal([[2, 2, 2],
                [4, 2, 6],
                [1, 8, 2]]), "Principal Diagonal win!")
print(diagonal([[1, 2, 2, 5, 1],
                [4, 1, 6, 1, 1],
                [1, 8, 5, 6, 2],
                [1, 5, 2, 1, 2],
                [1, 8, 2, 6, 1]]), "Secondary Diagonal win!")
print(diagonal([[1, 2, 2, 5, 1, 1, 2, 2, 5, 15],
                [4, 1, 6, 1, 1, 1, 2, 2, 1, 1],
                [1, 8, 1, 6, 2, 1, 2, 1, 5, 1],
                [1, 5, 2, 1, 2, 1, 1, 2, 5, 1],
                [1, 8, 2, 6, 1, 1, 2, 2, 5, 1],
                [1, 2, 2, 5, 1, 1, 2, 2, 5, 1],
                [1, 2, 2, 1, 1, 1, 1, 2, 5, 1],
                [1, 2, 1, 5, 1, 1, 2, 1, 5, 1],
                [1, 1, 2, 5, 1, 1, 2, 2, 1, 1],
                [1, 2, 2, 5, 1, 1, 2, 2, 5, 15]]), "Draw!")
print(diagonal([[1, 2, 2, 5, 1],
                [4, 1, 6, 1, 1],
                [1, 8, 5, 6, 2],
                [1, 5, 2, 1, 2],
                [1, 8, 2, 6, 1]]), "Secondary Diagonal win!")
print(diagonal([[1, 2, 2, 5, 1, 1, 2, 2, 5, 1],
                [4, 1, 6, 1, 1, 1, 2, 2, 1, 1],
                [1, 8, 1, 6, 2, 1, 2, 1, 5, 1],
                [1, 5, 2, 1, 2, 1, 1, 2, 5, 1],
                [1, 8, 2, 6, 1, 1, 2, 2, 5, 1],
                [1, 2, 2, 5, 1, 1, 2, 2, 5, 1],
                [1, 2, 2, 1, 1, 1, 1, 2, 5, 1],
                [1, 2, 1, 5, 1, 1, 2, 1, 5, 1],
                [1, 1, 2, 5, 1, 1, 2, 2, 1, 1],
                [1, 2, 2, 5, 1, 1, 2, 2, 5, 1]]), "Draw!")
