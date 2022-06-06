# 7 kyu
# Which triangle is that?


def type_of_triangle(a, b, c):
    for i in str(a) + str(b) + str(c):
        if not i.isdigit():
            return "Not a valid triangle"

    if a == b == c:
        return "Equilateral"
    elif a == b or b == c or a == c:
        return "Isosceles"
    return "Scalene"


print(type_of_triangle(1, 1, 1), "Equilateral")
print(type_of_triangle(3, 2, 4), "Scalene")
print(type_of_triangle(2, 2, 1), "Isosceles")
print(type_of_triangle('.', 5, 82), "Not a valid triangle")
