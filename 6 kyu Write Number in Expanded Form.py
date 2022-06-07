def expanded_form(num):
    lst = []
    while len(str(num)) > 1:
        lst.append(str(num % 10))
        num = int(str(num)[:-1])
    return lst
    # return int(str(num)[:-1])


print(expanded_form(12), '10 + 2')
print(expanded_form(42), '40 + 2')
print(expanded_form(70304), '70000 + 300 + 4')
