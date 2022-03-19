def riders(stations):
    riders = 1
    total = 0
    i = 0

    while i < len(stations):
        total += stations[i]
        if total > 100:
            total = 0
            i -= 1
            riders += 1
        i += 1

    return riders


print(riders([18, 15]), 1)
print(riders([43, 23, 40, 13]), 2)
print(riders([33, 8, 16, 47, 30, 30, 46]), 3)
print(riders([6, 24, 6, 8, 28, 8, 23, 47, 17, 29, 37, 18, 40, 49]), 4)
print(riders([49, 13, 26, 36, 22, 9, 43, 38, 30, 34]), 4)
