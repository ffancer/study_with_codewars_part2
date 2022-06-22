# 3 kyu
# How many are smaller than me II?


def smaller(arr):
    result = [0] * len(arr)
    root, index = None, len(arr) - 1
    while index >= 0:
        root = tree(root, index, arr[index], 0, result)
        index -= 1
    return result


class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value
        self.count = 0
        self.occurrences = 1


def tree(root, index, num, summ, result):
    if root is None:
        result[index] = summ
        return Node(num)
    if root.value == num:
        root.occurrences += 1
        result[index] = summ + root.count
    elif root.value > num:
        root.count += 1
        root.left = tree(root.left, index, num, summ, result)
    else:
        count = summ + root.count + root.occurrences
        root.right = tree(root.right, index, num, count, result)
    return root


print(smaller([5, 4, 3, 2, 1]), [4, 3, 2, 1, 0])
print(smaller([1, 2, 3]), [0, 0, 0])
print(smaller([1, 2, 0]), [1, 1, 0])
print(smaller([1, 2, 1]), [0, 1, 0])
print(smaller([1, 1, -1, 0, 0]), [3, 3, 0, 0, 0])
print(smaller([5, 4, 7, 9, 2, 4, 4, 5, 6]), [4, 1, 5, 5, 0, 0, 0, 0, 0])
print(smaller([5, 4, 7, 9, 2, 4, 1, 4, 5, 6]), [5, 2, 6, 6, 1, 1, 0, 0, 0, 0])
