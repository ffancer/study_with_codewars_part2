def array_packing(arr):
    lst = []

    for i in arr:
        lst.append(bin(i)[2:])

    return lst


print(array_packing([24, 85, 0]), 21784)
print(array_packing([23, 45, 39]), 2567447)
print(array_packing([1, 1]), 257)
print(array_packing([0]), 0)
print(array_packing([255, 255, 255, 255]), 4294967295)
