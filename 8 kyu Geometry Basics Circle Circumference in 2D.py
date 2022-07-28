# 8 kyu
# Geometry Basics: Circle Circumference in 2D

from math import pi


def circle_circumference(circle):
    return round(circle.radius * pi * 2, 6)


print(circle_circumference(10))
