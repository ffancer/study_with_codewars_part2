def least_larger(a, i):
    if max(a) == a[i]:
        return -1

    num = a[i]
    lst = sorted(a)
    for i, j in enumerate(lst):
        if j == num:
            if lst[i + 1] > num:
                return a.index(lst[i + 1])


print(least_larger([4, 1, 3, 5, 6], 0), 3)
print(least_larger([4, 1, 3, 5, 6], 4), -1)
print(least_larger([1, 3, 5, 2, 4], 0), 3)
