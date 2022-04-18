# 7 kyu
# Training JS #22: Unlock new skills--Arrow function,spread operator and deconstruction


def shuffle_it(*args):
    pass


print(shuffle_it([1, 2, 3, 4, 5], [1, 2]), [1, 3, 2, 4, 5])
print(shuffle_it([1, 2, 3, 4, 5], [1, 2], [3, 4]), [1, 3, 2, 5, 4])
print(shuffle_it([1, 2, 3, 4, 5], [1, 2], [3, 4], [2, 3]), [1, 3, 5, 2, 4])
print(shuffle_it([1, 2, 3, 4, 5], [4, 4]), [1, 2, 3, 4, 5])
print(shuffle_it([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])
