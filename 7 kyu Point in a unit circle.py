def point_in_circle(x, y):
    return x ** 2 + y ** 2 < 1


print(point_in_circle(0, 0), True)
print(point_in_circle(2, 0), False)
print(point_in_circle(-1.1, 0), False)
print(point_in_circle(0, 0.9), True)
print(point_in_circle(1, 0), False)
