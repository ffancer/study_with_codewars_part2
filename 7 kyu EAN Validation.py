def validate_ean(code):
    total = 0
    lst = []
    for i, j in enumerate(code):
        if i % 2 == 0:
            total += int(j) * 3
        else:
            total += i
    return total


print(validate_ean("400330101839"), True)
print(validate_ean("9783815820865"), True)
print(validate_ean("9783815820864"), False)
print(validate_ean("9783827317100"), True)
