def duplicate_elements(m, n):
    pass


print(duplicate_elements([1, 2, 3, 4, 5], [1, 6, 7, 8, 9]), True)
print(duplicate_elements([9, 8, 7], [8, 1, 3]), True)
print(duplicate_elements([-2, -4, -6, -8], [-2, -3, -5, -7]), True)
print(duplicate_elements([-9, -8, -7], [-8, -1, -3]), True)
print(duplicate_elements([1, 3, 5, 7, 9], [2, 4, 6, 8]), False)
print(duplicate_elements([9, 8, 7], [6, 5, 4]), False)
print(duplicate_elements([], [9, 8, 7, 6, 5]), False)
print(duplicate_elements([9, 8, 7, 6, 5], []), False)
print(duplicate_elements([], []), False)
