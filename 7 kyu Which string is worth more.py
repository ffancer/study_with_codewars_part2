# 7 kyu
# Which string is worth more?


def highest_value(a, b):
    total_a, total_b = 0, 0

    for i in a:
        total_a += ord(i)

    for i in b:
        total_b += ord(i)

    if total_a == total_b:
        return a
    elif total_a > total_b:
        return a
    return b


print(highest_value("AaBbCcXxYyZz0189", "KkLlMmNnOoPp4567"), "KkLlMmNnOoPp4567")
print(highest_value('d#', 'Q<'), 'Q<')
print(highest_value('HELLO$', '&(HELLO@#'), 'Q<')
