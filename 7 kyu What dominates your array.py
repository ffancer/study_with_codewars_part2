# 7 kyu
# What dominates your array?


def dominator(arr):
    if not arr:
        return -1

    dct = {}

    for i in arr:
        dct.update({i: arr.count(i)})

    for i, j in dct.items():
        if j > len(arr) // 2:
            return i
    return -1


print(dominator([3, 4, 3, 2, 3, 1, 3, 3]), 3)
print(dominator([1, 2, 3, 4, 5]), -1)
print(dominator([1, 1, 1, 2, 2, 2]), -1)
print(dominator([1, 1, 1, 2, 2, 2, 2]), 2)
print(dominator([]), -1)
