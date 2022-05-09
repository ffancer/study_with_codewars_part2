def area(d, l):
    s = l * (0.5 * (d ** 2 - l ** 2))
    return s
print(area(5, 4), 12)
print(area(10, 6), 48)
print(area(13, 5), 60)
print(area(12, 5), 54.54)
print(area(5, 5), "Not a rectangle")
print(area(3, 5), "Not a rectangle")
