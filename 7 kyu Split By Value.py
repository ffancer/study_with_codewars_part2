def split_by_value(k, elements):
    return [x for x in elements if x < k] + [x for x in elements if x >= k]


print(split_by_value(5, [1, 3, 5, 7, 6, 4, 2]), [1, 3, 4, 2, 5, 7, 6])
print(split_by_value(0, [5, 2, 7, 3, 2]), [5, 2, 7, 3, 2])
print(split_by_value(6, [6, 4, 10, 10, 6]), [4, 6, 10, 10, 6])
