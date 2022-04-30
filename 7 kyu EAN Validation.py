def validate_ean(code):
    total = sum(int(j) * 3 if i % 2 != 0 else int(j) for i, j in enumerate(code[:-1])) % 10
    return 10 - total == int(code[-1]) if total > 0 else total == int(code[-1])


print(validate_ean("400330101839"), True)
print(validate_ean("9783815820865"), True)
print(validate_ean("9783815820864"), False)
print(validate_ean("9783827317100"), True)
