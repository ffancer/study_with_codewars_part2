def bubblesort_once(l):
    lst = l[:]

    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[j - 1] > lst[j]:
                lst[j], lst[j - 1] = lst[j - 1], lst[j]
        return lst
    return []


print(bubblesort_once([9, 7, 5, 3, 1, 2, 4, 6, 8]), [7, 5, 3, 1, 2, 4, 6, 8, 9])
