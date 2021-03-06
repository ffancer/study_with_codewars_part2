def sticky_calc(operation, val1, val2):
    return round(eval("{0}{1}{2}{1}".format(round(val1), round(val2), operation)))


print(sticky_calc('+', 4, 7), 54)
print(sticky_calc('-', 15, 10), 1500)
print(sticky_calc('*', 5, 5), 275)
print(sticky_calc('/', 10, 7), 15)
# Note How numbers are rounded
print(sticky_calc('+', 4.2, 7), 54)  # Output : (47) + 7 = 54
print(sticky_calc('+', 4.7, 7.2), 64)  # Output : (57) + 7 = 54
# Note that non-integer outputs are rounded
print(sticky_calc('/', 10, 7), 15)
# Added to enforce rounding and not flooring
print(sticky_calc('/', 51, 63), 82)


