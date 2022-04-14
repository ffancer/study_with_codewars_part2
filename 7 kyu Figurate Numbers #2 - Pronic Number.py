def is_pronic(n):
    flag = False

    for j in range(1, n + 1):
        if j * (j + 1) == n:
            flag = True
            break

    return flag


print(is_pronic(0), True, '0 is a Pronic Number')
print(is_pronic(1), False, '1 is not a Pronic Number')
print(is_pronic(2), True, '2 is a Pronic Number')
print(is_pronic(3), False, '3 is not a Pronic Number')
print(is_pronic(4), False, '4 is not a Pronic Number')
print(is_pronic(5), False, '5 is not a Pronic Number')
print(is_pronic(6), True, '6 is a Pronic Number')
print(is_pronic(-3), False, '-3 is not a Pronic Number')
print(is_pronic(-27), False, '-27 is not a Pronic Number')
