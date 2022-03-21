def convert_bits(a, b):
    a = bin(a)[2:].zfill(32)
    b = bin(b)[2:].zfill(32)
    #
    c = a.count('0') + a.count('1')
    d = b.count('0') + b.count('1')
    return c, d
    # return a, b

print(convert_bits(31, 14), 2)
# print(convert_bits(7, 17), 3)
# print(convert_bits(31, 0), 5)
# print(convert_bits(0, 0), 0)
