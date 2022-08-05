weapons_dct = {
    'PT92': 17,
    'M4A1': 30,
    'M16A2': 30,
    'PSG1': 5
}


def mag_number(str_, int_):
    # return weapons_dct[str_] * 3 / int_
    # return weapons_dct[int_]

    return int_ * 3 / weapons_dct[str_]

print(mag_number("PT92", 6), 2)
print(mag_number("M4A1", 8), 1)
print(mag_number("M16A2", 19), 2)
print(mag_number("PSG1", 31), 19)
print(mag_number("PT92", 19), 4)
