from math import tan, pi


def circle_diameter(sides, side_length):
    return side_length / (tan((180 / sides) * pi / 180))


print(circle_diameter(4, 5), 5.000)
print(circle_diameter(8, 9), 21.728)
print(circle_diameter(3, 4), 2.309)
