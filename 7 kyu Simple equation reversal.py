def solve(eq):
    lst = []
    s1 = ''
    s2 = ''

    for i in eq:
        if i.isalnum():
            s1 += i
        elif i in '*+-/':
            s2 = i
            lst.append(s1)
            lst.append(s2)
            s1 = ''
            s2 = ''
    lst.append(s1)

    return ''.join(lst[::-1])


print(solve("100*b/y"), "y/b*100")
print(solve("a+b-c/d*30"), "30*d/c-b+a")
print(solve("a*b/c+50"), "50+c/b*a")
