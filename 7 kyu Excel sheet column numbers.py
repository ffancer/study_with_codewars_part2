def title_to_number(title):
    ret = 0

    for i in title:
        ret = ret * 26 + ord(i) - 64

    return ret


print(title_to_number('A'), 1)
print(title_to_number('Z'), 26)
print(title_to_number('AA'), 27)
print(title_to_number('AZ'), 52)
print(title_to_number('BA'), 53)
