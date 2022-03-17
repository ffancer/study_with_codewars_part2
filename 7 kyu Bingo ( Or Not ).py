def bingo(array):
    cnt_bingo = 0

    for i in [2, 7, 9, 14, 15]:
        if i in array:
            cnt_bingo += 1

    return 'WIN' if cnt_bingo >= 5 else 'LOSE'


print(bingo([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), "LOSE")
print(bingo([20, 12, 23, 14, 6, 22, 12, 17, 2, 26]), "LOSE")
print(bingo([1, 2, 3, 7, 5, 14, 7, 15, 9, 10]), "WIN")
print(bingo([5, 2, 13, 7, 5, 14, 17, 15, 9, 10]), "WIN")
