def elimination(arr):
    for x in arr:
        if arr.count(x) == 2:
            return x


print(elimination([2, 5, 34, 1, 22, 1]), 1, "twins are 1s")
print(elimination([2, 2, 34, 1, 22]), 2, "twins are 2s")
print(elimination([2, 5, 34, 1, 22]), None, "There are no twins in the city")
print(elimination(
    [84, 73, 9, 26, 31, 87, 22, 50, 20, 6, 30, 55, 40, 14, 58, 3, 44, 97, 57, 67, 60, 83, 13, 7, 19, 99, 77, 71, 68, 33,
     36, 35, 81, 80, 83, 42, 4, 79, 47, 45, 65, 52]), 83)
