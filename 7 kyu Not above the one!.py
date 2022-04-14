def binary_cleaner(seq):
    lst1, lst2 = [], []

    for i in range(len(seq)):
        if seq[i] <= 1:
            lst1.append(seq[i])
        else:
            lst2.append(i)

    return lst1, lst2


print(binary_cleaner([0, 1, 2, 1, 0, 2, 1, 1, 1, 0, 4, 5, 6, 2, 1, 1, 0]),
      ([0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0], [2, 5, 10, 11, 12, 13]))
print(binary_cleaner([0, 1, 1, 2, 0]), ([0, 1, 1, 0], [3]))
print(binary_cleaner([2, 2, 0]), ([0], [0, 1]))
print(binary_cleaner([0, 1, 2, 1, 0, 2, 1, 1]), ([0, 1, 1, 0, 1, 1], [2, 5]))
print(binary_cleaner([1]), ([1], []))
