def alternate_sq_sum(arr):
    total = 0

    for i, j in enumerate(arr):
        if i % 2 == 0:
            total += j
        else:
            total += j ** 2

    return total


print(alternate_sq_sum([]), 0)
print(alternate_sq_sum([-1, 0, -3, 0, -5, 3]), 0)
print(alternate_sq_sum([-1, 2, -3, 4, -5]), 11)
print(alternate_sq_sum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 245)
