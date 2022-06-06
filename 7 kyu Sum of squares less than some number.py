def get_number_of_squares(n):
    total = 0

    for i in range(1, n+1):
        total += i ** 2

    return total


print(get_number_of_squares(1))
print(get_number_of_squares(2))
print(get_number_of_squares(5))
print(get_number_of_squares(6))
print(get_number_of_squares(15))
