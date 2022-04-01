# 7 kyu
# What dominates your array?

from collections import Counter

def dominator(arr):
    return Counter(arr)


print(dominator([3, 4, 3, 2, 3, 1, 3, 3]), 3)
print(dominator([1, 2, 3, 4, 5]), -1)
print(dominator([1, 1, 1, 2, 2, 2]), -1)
print(dominator([1, 1, 1, 2, 2, 2, 2]), 2)
# print(dominator([]), -1)
