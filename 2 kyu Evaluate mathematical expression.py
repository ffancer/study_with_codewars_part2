def calc(expression):
    ex = list(expression.replace(' ', ''))

    def peek():
        return ex[0] if ex else ''

    def get():
        return ex.pop(0)

    def number():
        result = get()
        while peek() >= '0' and peek() <= '9' or peek() == '.':
            result += get()
        return float(result)

    def factor():
        if peek() >= '0' and peek() <= '9':
            return number()
        elif peek() == '(':
            get()  # '('
            result = expression()
            get()  # ')'
            return result
        elif peek() == '-':
            get()
            return -factor()
        return 0  # error

    def term():
        result = factor()
        while peek() == '*' or peek() == '/':
            if get() == '*':
                result *= factor()
            else:
                result /= factor()
        return result

    def expression():
        result = term()
        while peek() == '+' or peek() == '-':
            if get() == '+':
                result += term()
            else:
                result -= term()
        return result

    return expression()


print(calc("1 + 1"), 2)
print(calc("8/16"), 0.5)
print(calc("3 -(-1)"), 4)
print(calc("2 + -2"), 0)
print(calc("10- 2- -5"), 13)
print(calc("(((10)))"), 10)
print(calc("3 * 5"), 15)
print(calc("-7 * -(6 / 3)"), 14)
