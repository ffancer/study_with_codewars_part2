def all_non_consecutive(arr):
    lst = []

    if len(arr) <= 1:
        return lst

    first = arr[0]

    for i, j in enumerate(arr):
        if first != j:
            lst.append({'i': i, 'n': j})
            first = j
        first += 1

    return lst


print(all_non_consecutive([1, 2, 3, 4, 6, 7, 8, 10]), [{'i': 4, 'n': 6}, {'i': 7, 'n': 10}])
