def is_triangular(t):
    x = int((t * 2) ** 0.5)
    return t == x * (x + 1) / 2


print(is_triangular(1), True, "Failed when t = 1")
print(is_triangular(3), True, "Failed when t = 3")
print(is_triangular(6), True, "Failed when t = 6")
print(is_triangular(10), True, "Failed when t = 10")
print(is_triangular(15), True, "Failed when t = 15")
print(is_triangular(21), True, "Failed when t = 21")
print(is_triangular(28), True, "Failed when t = 28")

print(is_triangular(2), False, "Failed when t = 2")
print(is_triangular(7), False, "Failed when t = 7")
print(is_triangular(14), False, "Failed when t = 14")
print(is_triangular(27), False, "Failed when t = 27")
