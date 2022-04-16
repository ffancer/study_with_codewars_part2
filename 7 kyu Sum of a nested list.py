def sum_nested(lst):
    total = 0

    for i in lst:
        if not i:
            continue
        if type(i) == list:
            total += sum_nested(i)
        else:
            total += i  # coz type(i) == int

    return total


print(sum_nested([1]), 1)
print(sum_nested([1, 2, 3, 4]), 10)
print(sum_nested(list(range(11))), 55)
print(sum_nested([]), 0)
print(sum_nested([[1], []]), 1)
print(sum_nested([[1, 2, 3, 4]]), 10)
print(sum_nested([[], []]), 0)
print(sum_nested([1, [1], [[1]], [[[1]]]]), 4)
print(sum_nested([1, [1], [1, [1]], [1, [1], [1, [1]]]]), 8)
print(sum_nested([[[[], [], [[[[[[[[[[]]]]]]]]]]], [], [], [[[], [[]]]]], []]), 0)
