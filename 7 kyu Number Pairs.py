def get_larger_numbers(a, b):
    lst = []

    for i in range(len(a)):
        if a[i] > b[i]:
            lst.append(a[i])
        else:
            lst.append(b[i])

    return lst


a = [13, 64, 15, 17, 88]
b = [23, 14, 53, 17, 80]
print(get_larger_numbers(a, b), [23, 64, 53, 17, 88], "Wrong result for a = {}, b = {}".format(a, b))
a = [34, -64, 15, 17, 88]
b = [23, 14, 53, 17, 80]
print(get_larger_numbers(a, b), [34, 14, 53, 17, 88], "Wrong result for a = {}, b = {}".format(a, b))
