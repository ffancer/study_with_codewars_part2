import math


def circle_diameter(sides, side_length):
    return side_length // (math.tan((180 / sides) * math.pi / 180))


print(circle_diameter(4, 5), 5.000)
print(circle_diameter(8, 9), 21.728)
print(circle_diameter(3, 4), 2.309)
