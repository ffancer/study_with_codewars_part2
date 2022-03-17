def pendulum(values):
    lst_middle = [min(values)]
    values.remove(min(values))
    lst_left, lst_right = [], []
    cnt = 0

    while values:
        min_val = min(values)
        if cnt % 2 == 0:
            lst_right.append(min_val)
        else:
            lst_left.append(min_val)
        cnt += 1
        values.remove(min(values))

    return lst_left[::-1] + lst_middle + lst_right

print(pendulum([4, 6, 8, 7, 5]), [8, 6, 4, 5, 7])
print(pendulum([19, 30, 16, 19, 28, 26, 28, 17, 21, 17]), [28, 26, 19, 17, 16, 17, 19, 21, 28, 30])
print(pendulum([-9, -2, -10, -6]), [-6, -10, -9, -2])
print(pendulum([-19, -9, -5, -6, -15, -16, -5, -12]), [-5, -9, -15, -19, -16, -12, -6, -5])
print(pendulum([11, -16, -18, 13, -11, -12, 3, 18]), [13, 3, -12, -18, -16, -11, 11, 18])
