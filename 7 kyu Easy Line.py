def easyline(n):
    return easyline(n - 1) * (4 * n - 2) // n if n else 1


print(easyline(7), 3432)
print(easyline(13), 10400600)
print(easyline(17), 2333606220)
print(easyline(19), 35345263800)
