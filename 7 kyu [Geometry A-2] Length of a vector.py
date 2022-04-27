# 7 kyu
# [Geometry A-2]: Length of a vector

from math import hypot


def vector_length(vector):
    x1, x2, y1, y2 = vector[0][0], vector[1][0], vector[0][1], vector[1][1]
    return hypot((x2-x1),(y2-y1))


print(vector_length([[0, 1], [0, 0]]), 1)
print(vector_length([[0, 3], [4, 0]]), 5)
print(vector_length([[1, -1], [1, -1]]), 0)
