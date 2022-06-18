def temp_check(board):
    temp = [i for i in range(1, 10)]

    for i in board:
        if sorted(i) != temp:
            return False


def valid_solution(board):
    if temp_check(board) == 0:
        return False

    alt_board = [[] for i in range(1, 10)]
    for i, j in enumerate(board):
        for k in range(0, 9):
            alt_board[i].append(board[k][i])

    if temp_check(alt_board) == 0:
        return False

    alt_board = []
    for i in board:
        for j in i:
            alt_board.append(j)

    square_board = [[] for i in range(0, 3)]
    x_board = []
    for i in alt_board:
        for j in range(0, 3):
            for k in range(0, 3):
                for h in range(0, 3):
                    square_board[k].append(alt_board.pop(0))
        x_board.append(square_board)
        square_board = [[] for i in range(0, 3)]

    square_board = []
    for i in x_board:
        for j in i:
            square_board.append(j)

    if temp_check(square_board) == 0:
        return False

    return True


print(valid_solution([[5, 3, 4, 6, 7, 8, 9, 1, 2],
                      [6, 7, 2, 1, 9, 5, 3, 4, 8],
                      [1, 9, 8, 3, 4, 2, 5, 6, 7],
                      [8, 5, 9, 7, 6, 1, 4, 2, 3],
                      [4, 2, 6, 8, 5, 3, 7, 9, 1],
                      [7, 1, 3, 9, 2, 4, 8, 5, 6],
                      [9, 6, 1, 5, 3, 7, 2, 8, 4],
                      [2, 8, 7, 4, 1, 9, 6, 3, 5],
                      [3, 4, 5, 2, 8, 6, 1, 7, 9]]), True)

print(valid_solution([[5, 3, 4, 6, 7, 8, 9, 1, 2],
                      [6, 7, 2, 1, 9, 0, 3, 4, 9],
                      [1, 0, 0, 3, 4, 2, 5, 6, 0],
                      [8, 5, 9, 7, 6, 1, 0, 2, 0],
                      [4, 2, 6, 8, 5, 3, 7, 9, 1],
                      [7, 1, 3, 9, 2, 4, 8, 5, 6],
                      [9, 0, 1, 5, 3, 7, 2, 1, 4],
                      [2, 8, 7, 4, 1, 9, 6, 3, 5],
                      [3, 0, 0, 4, 8, 1, 1, 7, 9]]), False)
