def sum_of_intervals(intervals):
    result = set()

    for start, stop in intervals:
        for x in range(start, stop):
            result.add(x)

    return len(result)


print(sum_of_intervals([(1, 5)]), 4)
print(sum_of_intervals([(1, 5), (6, 10)]), 8)
print(sum_of_intervals([(1, 5), (1, 5)]), 4)
print(sum_of_intervals([(1, 4), (7, 10), (3, 5)]), 7)
