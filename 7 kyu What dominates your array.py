# 7 kyu
# What dominates your array?


from collections import Counter


def dominator(arr):
    if not arr:
        return -1
    for i, j in Counter(arr).items():
        print(i, j)


print(dominator([3, 4, 3, 2, 3, 1, 3, 3]), 3)
print(dominator([1, 2, 3, 4, 5]), -1)
print(dominator([1, 1, 1, 2, 2, 2]), -1)
print(dominator([1, 1, 1, 2, 2, 2, 2]), 2)
print(dominator([]), -1)
