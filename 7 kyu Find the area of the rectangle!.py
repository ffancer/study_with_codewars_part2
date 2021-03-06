def area(d, l):
    try:
        s = l * pow((d ** 2 - l ** 2), 0.5)
        return round(s, 2) if s > 0 else 'Not a rectangle'
    except TypeError:
        return 'Not a rectangle'


print(area(5, 4), 12)
print(area(10, 6), 48)
print(area(13, 5), 60)
print(area(12, 5), 54.54)
print(area(5, 5), "Not a rectangle")
print(area(3, 5), "Not a rectangle")
