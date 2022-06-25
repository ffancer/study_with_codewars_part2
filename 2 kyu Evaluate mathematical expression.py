def calc(expression):
    # return eval("-7 * -(6 / 3)")
    return compile(expression)
    # return exec(expression)


print(calc("1 + 1"), 2)
print(calc("8/16"), 0.5)
print(calc("3 -(-1)"), 4)
print(calc("2 + -2"), 0)
print(calc("10- 2- -5"), 13)
print(calc("(((10)))"), 10)
print(calc("3 * 5"), 15)
print(calc("-7 * -(6 / 3)"), 14)
