def expanded_form(num):
    s = str(num)
    len_s = len(s)
    lst = []

    for i in range(0, len_s):
        if s[i] != '0':
            temp = s[i].ljust(len_s - i, '0')
            lst.append(temp)

    return ' + '.join(lst)


print(expanded_form(12), '10 + 2')
print(expanded_form(42), '40 + 2')
print(expanded_form(70304), '70000 + 300 + 4')
