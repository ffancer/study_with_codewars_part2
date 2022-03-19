def riders(stations):
    riders = 1
    ostatok = 0
    summa = 0
    for i in stations:
        summa += i

        if summa > 100:
            riders += 1
            ostatok += summa - 100
            summa = 0
    if summa + ostatok >= 100:
        riders += (summa + ostatok) // 100

    return riders


print(riders([18, 15]), 1)
print(riders([43, 23, 40, 13]), 2)
print(riders([33, 8, 16, 47, 30, 30, 46]), 3)
print(riders([6, 24, 6, 8, 28, 8, 23, 47, 17, 29, 37, 18, 40, 49]), 4)
print(riders([49, 13, 26, 36, 22, 9, 43, 38, 30, 34]), 4)
