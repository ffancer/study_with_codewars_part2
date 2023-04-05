def array_packing(arr):
    lst = []
    num = ''

    for i in arr:
        lst.append(bin(i)[2:])

    for j in lst:
        num += j

    return int(num, 2)


print(array_packing([24, 85, 0]), 21784)
print(array_packing([23, 45, 39]), 2567447)
print(array_packing([1, 1]), 257)
print(array_packing([0]), 0)
print(array_packing([255, 255, 255, 255]), 4294967295)


# print(bin(24)[2:], bin(85)[2:])
# print(bin(int('11000', 2) + int('1010101', 2))[2:])
# print(int('000000000101010100011000', 2))