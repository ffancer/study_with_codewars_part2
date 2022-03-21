def convert_bits(a, b):
    a = abs(len(bin(a)[2:]) - len(bin(b)[2:]))
    cnt = 0
    for i in bin(a)[2:]:
        if i not in bin(b)[2:]:
            cnt += 1
    return cnt


print(convert_bits(31, 14), 2)
# print(convert_bits(7, 17), 3)
# print(convert_bits(31, 0), 5)
# print(convert_bits(0, 0), 0)
