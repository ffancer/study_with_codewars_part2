# 7 kyu
# Which string is worth more?


def highest_value(a, b):
    total_a, total_b = 0, 0

    for i in a:
        if i.isalpha():
            total_a += ord(i)

    return total_a


print(highest_value("AaBbCcXxYyZz0189", "KkLlMmNnOoPp4567"), "KkLlMmNnOoPp4567")
