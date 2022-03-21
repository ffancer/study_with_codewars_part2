def all_non_consecutive(arr):
    lst = []

    for i in range(min(arr), max(arr) + 1):
        lst.append(i)

    return lst


print(all_non_consecutive([1, 2, 3, 4, 6, 7, 8, 10]), [{'i': 4, 'n': 6}, {'i': 7, 'n': 10}])
