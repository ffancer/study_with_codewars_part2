def alternate_sq_sum(arr):
    for i, j in enumerate(arr):
        print(i, j)


print(alternate_sq_sum([]), 0)
print(alternate_sq_sum([-1, 0, -3, 0, -5, 3]), 0)
print(alternate_sq_sum([-1, 2, -3, 4, -5]), 11)
print(alternate_sq_sum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 245)
