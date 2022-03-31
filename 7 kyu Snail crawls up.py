def snail(column, day, night):
    cnt = 0
    while column > 0:
        column -= day
        column += night
        cnt += 1

    return cnt


print(snail(3, 2, 1), 2)
print(snail(10, 3, 1), 5)
print(snail(10, 3, 2), 8)
print(snail(100, 20, 5), 7)
print(snail(5, 10, 3), 1)
