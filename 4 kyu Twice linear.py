def dbl_linear(n):
    cnt_y, cnt_z = 0, 0
    lst = [1]

    while len(lst) <= n:
        y = 2 * lst[cnt_y] + 1
        z = 3 * lst[cnt_z] + 1

        if y > z:
            lst.append(z)
            cnt_z += 1
        elif y < z:
            lst.append(y)
            cnt_y += 1
        else:
            lst.append(y)
            cnt_y += 1
            cnt_z += 1

    return lst[n]


print(dbl_linear(10), 22)
print(dbl_linear(20), 57)
print(dbl_linear(30), 91)
print(dbl_linear(50), 175)
