def split_by_value(k, elements):
    first_lst, middle_lst, last_lst = [], [], []

    for i in elements:
        if i < k:
            first_lst.append(i)
        if i > k:
            middle_lst.append(i)
        if i == k:
            last_lst.append(i)

    return first_lst + middle_lst + last_lst


print(split_by_value(5, [1, 3, 5, 7, 6, 4, 2]), [1, 3, 4, 2, 5, 7, 6])
print(split_by_value(0, [5, 2, 7, 3, 2]), [5, 2, 7, 3, 2])
print(split_by_value(6, [6, 4, 10, 10, 6]), [4, 6, 10, 10, 6])
