def get_number_of_squares(n):
    total = 0
    cnt = 0

    while total < n:
        cnt += 1
        total += pow(cnt, 2)

    return cnt - 1


print(get_number_of_squares(1))
print(get_number_of_squares(2))
print(get_number_of_squares(5))
print(get_number_of_squares(6))
print(get_number_of_squares(15))
