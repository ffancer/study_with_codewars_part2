def passed(lst):
    cnt = 0
    total = 0

    for i in lst:
        if i < 19:
            total += i
            cnt += 1

    if cnt == 0:
        return 'No pass scores registered.'
    return int(total / cnt + .5)


print(passed([10, 10, 10, 18, 20, 20]), 12)
print(passed([21, 22, 24]), 'No pass scores registered.')
print(passed([3, 22, 9, 13, 20, 18, 2, 14, 20, 8, 23, 12, 7, 21, 21, 19, 20, 11, 18, 7, 13, 22, 11, 20, 9]), 10)
print(passed([19, 16, 8, 11, 25, 10, 29, 22, 23]), 11)
