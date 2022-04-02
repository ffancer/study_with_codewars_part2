def sort_by_value_and_index(arr):
    arr_calc = map(lambda i, n: n * (i + 1), range(len(arr)), arr)
    return [x for (y, x) in sorted(zip(arr_calc, arr), key=lambda pair: pair[0])]


print(sort_by_value_and_index([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])
print(sort_by_value_and_index([23, 2, 3, 4, 5]), [2, 3, 4, 23, 5])
print(sort_by_value_and_index([26, 2, 3, 4, 5]), [2, 3, 4, 5, 26])
print(sort_by_value_and_index([9, 5, 1, 4, 3]), [1, 9, 5, 3, 4])
