# 7 kyu
# [Geometry A-2]: Length of a vector

from math import hypot


def vector_length(vector):
    return hypot((vector[0]-vector[2]),(vector[1]-vector[3]))


print(vector_length([[0, 1], [0, 0]]), 1)
print(vector_length([[0, 3], [4, 0]]), 5)
print(vector_length([[1, -1], [1, -1]]), 0)
