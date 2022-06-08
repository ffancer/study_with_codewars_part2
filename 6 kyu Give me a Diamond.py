def diamond(n):
    # Make some diamonds!
    return "*"


expected = " *\n"
expected += "***\n"
expected += " *\n"
print(diamond(1), "*\n")
print(diamond(2), None)
print(diamond(3), expected)
print(diamond(5), "  *\n ***\n*****\n ***\n  *\n")
print(diamond(0), None)
print(diamond(-3), None)
