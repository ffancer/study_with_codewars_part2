def pendulum(values):
    # sorted_values = sorted(values)
    middle_lst = [sorted(values)[0]]
    right_lst = sorted(values)[1::2]
    left_lst = sorted(values)[2::2]
    return left_lst[::-1] + middle_lst + right_lst


print(pendulum([4, 6, 8, 7, 5]), [8, 6, 4, 5, 7])
print(pendulum([19, 30, 16, 19, 28, 26, 28, 17, 21, 17]), [28, 26, 19, 17, 16, 17, 19, 21, 28, 30])
print(pendulum([-9, -2, -10, -6]), [-6, -10, -9, -2])
print(pendulum([-19, -9, -5, -6, -15, -16, -5, -12]), [-5, -9, -15, -19, -16, -12, -6, -5])
print(pendulum([11, -16, -18, 13, -11, -12, 3, 18]), [13, 3, -12, -18, -16, -11, 11, 18])
