def mirror(data: list) -> list:
    arr = sorted(data)
    return arr + arr[-2::-1]


print(mirror([]), [])
print(mirror([1]), [1])
print(mirror([2, 1]), [1, 2, 1])
print(mirror([1, 3, 2]), [1, 2, 3, 2, 1])
print(mirror([-8, 42, 18, 0, -16]), [-16, -8, 0, 18, 42, 18, 0, -8, -16])
print(mirror([-3, 15, 8, -1, 7, -1]), [-3, -1, -1, 7, 8, 15, 8, 7, -1, -1, -3])
