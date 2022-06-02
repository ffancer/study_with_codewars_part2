def euclidean_distance(point1, point2):
    return round(sum((b - a) ** 2 for a, b in zip(point1, point2)) ** 0.5, 2)


point1 = (-1,)
point2 = (2,)
print(euclidean_distance(point1, point2), 3.0)

point1 = (-1, 2)
point2 = (2, 4)
print(euclidean_distance(point1, point2), 3.61)

point1 = (-1, 2, 5)
point2 = (2, 4, 9)
print(euclidean_distance(point1, point2), 5.39)
