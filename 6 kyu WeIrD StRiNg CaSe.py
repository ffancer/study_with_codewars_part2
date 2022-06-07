def to_weird_case(string):
    lst = string.split()
    ans = []

    for i in lst:
        s = ''
        for k, j in enumerate(i):
            if k % 2 == 0:
                s += j.upper()
            else:
                s += j
        ans.append(s)

    return ' '.join(ans)


print(to_weird_case('This'), 'ThIs')
print(to_weird_case('is'), 'Is')
print(to_weird_case('This is a test'), 'ThIs Is A TeSt')
