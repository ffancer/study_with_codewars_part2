def sum_of_digits(digits):
    try:
        if type(digits) is not str:
            digits = str(digits)

        lst = []

        for i in digits:
            lst.append(i)

        return ' + '.join(lst) + ' = ' + str(sum(int(i) for i in lst))
    except ValueError:
        return ''



print(sum_of_digits("3433"), "3 + 4 + 3 + 3 = 13")
print(sum_of_digits("64323"), "6 + 4 + 3 + 2 + 3 = 18")
print(sum_of_digits("8"), "8 = 8")
print(sum_of_digits(3433), "3 + 4 + 3 + 3 = 13")
print(sum_of_digits(64323), "6 + 4 + 3 + 2 + 3 = 18")
print(sum_of_digits(8), "8 = 8")
print(sum_of_digits(None), "")
