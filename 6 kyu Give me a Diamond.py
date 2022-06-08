def diamond(n):
    up_s, down_s, mid_s = '', '', n * '*'

    for i in range(1, n, 2):
        up_s += " " * ((n - i) // 2) + "*" * i + "\n"

    return up_s


# expected = " *\n"
# expected += "***\n"
# expected += " *\n"
# print(diamond(1), "*\n")
# print(diamond(2), None)
# print(diamond(3), expected)
# print(diamond(5), "  *\n ***\n*****\n ***\n  *\n")
# print(diamond(0), None)
# print(diamond(-3), None)
print(diamond(7))

