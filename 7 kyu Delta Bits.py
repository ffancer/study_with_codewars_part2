def convert_bits(a, b):
    a = bin(a)[2:].zfill(32)
    b = bin(b)[2:].zfill(32)

    return sum(1 for i, j in zip(a, b) if i != j)

print(convert_bits(31, 14), 2)
print(convert_bits(7, 17), 3)
print(convert_bits(31, 0), 5)
print(convert_bits(0, 0), 0)
