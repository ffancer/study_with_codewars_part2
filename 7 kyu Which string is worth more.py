# 7 kyu
# Which string is worth more?


def highest_value(a, b):
    total_a = sum(ord(i) for i in a)
    total_b = sum(ord(i) for i in b)
    return a if total_a >= total_b else b


print(highest_value("AaBbCcXxYyZz0189", "KkLlMmNnOoPp4567"), "KkLlMmNnOoPp4567")
print(highest_value('d#', 'Q<'), 'Q<')
print(highest_value('HELLO$', '&(HELLO@#'), 'Q<')
