def calc(l):
    while ')' in l:
        for i, c in enumerate(l):
            if c == '(': lastopen = i
            if c == ')':
                l = l[:lastopen] + str(calc(l[lastopen + 1:i])) + l[i + 1:]
                break

    stack = []
    for t in tokens(l):
        if stack and (stack[-1] == '*' or stack[-1] == '/'):
            op, a = stack.pop(), stack.pop()
            t = a / t if op == '/' else a * t
        stack.append(t)

    stack = stack[::-1]

    a = 0 if stack[-1] in ['+', '-'] else stack.pop()

    while stack:
        op, t = stack.pop(), stack.pop()
        a = a + t if op == '+' else a - t

    return a


def tokens(s):
    R = [('--', '+'), ('+-', '-'), ('++', '+'), ('-+', '-'), ('*+', '*'), ('/+', '/')]

    s = ''.join(s.split())
    while any(f in s for f, _ in R):
        for f, r in R: s = s.replace(f, r)

    for t in '*/-+':
        s = s.replace(t, ' ' + t + ' ')
    s = s.replace('  ', ' ').replace('* - ', '* -').replace('/ - ', '/ -')

    return [t if t in '*/+-' else float(t) if '.' in t else int(t) for t in s.split()]


print(calc("1 + 1"), 2)
print(calc("8/16"), 0.5)
print(calc("3 -(-1)"), 4)
print(calc("2 + -2"), 0)
print(calc("10- 2- -5"), 13)
print(calc("(((10)))"), 10)
print(calc("3 * 5"), 15)
print(calc("-7 * -(6 / 3)"), 14)
