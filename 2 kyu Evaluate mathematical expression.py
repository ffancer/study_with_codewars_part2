OPERATORS = {'+': (1, lambda x, y: x + y), '-': (1, lambda x, y: x - y),
             '*': (2, lambda x, y: x * y), '/': (2, lambda x, y: x / y)}


def eval_(formula):
    def parse(line):
        line = line.replace(' ', '')
        num = ''
        for i in line:
            if not num and i in '-':
                num += i
                continue
            if i in '1234567890.':
                num += i
            elif num:
                yield float(num)
                num = ''
            if i in OPERATORS or i in '()':
                yield i
        if num:
            yield float(num)

    def shunting_yard(parsed_formula):
        stack = []
        for token in parsed_formula:
            if token in OPERATORS:
                while stack and stack[-1] != "(" and OPERATORS[token][0] <= OPERATORS[stack[-1]][0]:
                    yield stack.pop()
                stack.append(token)
            elif token == ")":
                while stack:
                    x = stack.pop()
                    if x == "(":
                        break
                    yield x
            elif token == "(":
                stack.append(token)
            else:
                yield token
        while stack:
            yield stack.pop()

    def calc(polish):
        stack = []
        for token in polish:
            if token in OPERATORS:
                y, x = stack.pop(), stack.pop()
                stack.append(OPERATORS[token][1](x, y))
            else:
                stack.append(token)
        return stack[0]

    return calc(shunting_yard(parse(formula)))



def calc(expression):
    # expression = expression.replace(' ', '')
    return eval_(expression)


print(calc("1 + 1"), 2)
print(calc("8/16"), 0.5)
print(calc("3 -(-1)"), 4)
print(calc("2 + -2"), 0)
print(calc("10- 2- -5"), 13)
print(calc("(((10)))"), 10)
print(calc("3 * 5"), 15)
print(calc("-7 * -(6 / 3)"), 14)
