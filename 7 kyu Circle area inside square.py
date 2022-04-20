from cmath import pi
from math import sqrt


def square_area_to_circle(size):
    return (sqrt(size) / 2) ** 2 * pi


print(square_area_to_circle(9))
print(square_area_to_circle(20))
