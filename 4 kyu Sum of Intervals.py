def sum_of_intervals(intervals):
    max_num, min_num = 0, 0
    lst = []

    for i in intervals:
        if i[1] > max_num:
            max_num = i[1]
        if i[0] < min_num:
            min_num = i[0]

    for i in range(0, max_num - min_num):
        lst.append(0)
    for i in intervals:
        for j in range(i[0]-min_num, i[1]-min_num):
            lst[j] = 1

    return sum(lst)


print(sum_of_intervals([(1, 5)]), 4)
print(sum_of_intervals([(1, 5), (6, 10)]), 8)
print(sum_of_intervals([(1, 5), (1, 5)]), 4)
print(sum_of_intervals([(1, 4), (7, 10), (3, 5)]), 7)
