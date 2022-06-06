import math


def coordinates(degrees, radius):
    x = math.cos(degrees * math.pi / 180) * radius
    y = math.sin(degrees * math.pi / 180) * radius
    return x, y

print(coordinates(90, 1), (0.0, 1.0))
