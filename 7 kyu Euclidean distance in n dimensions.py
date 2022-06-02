from math import hypot


def euclidean_distance(point1, point2):
    for i in range(len(point1)):
        return hypot(point1[i] - point1[i-1], point2[i] - point2[i-1])


point1 = (-1,)
point2 = (2,)
print(euclidean_distance(point1, point2), 3.0)

point1 = (-1, 2)
point2 = (2, 4)
print(euclidean_distance(point1, point2), 3.61)

point1 = (-1, 2, 5)
point2 = (2, 4, 9)
print(euclidean_distance(point1, point2), 5.39)
