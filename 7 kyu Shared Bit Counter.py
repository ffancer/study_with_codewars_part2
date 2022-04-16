def shared_bits(a, b):
    return bin(a & b).count('1') > 1


print(shared_bits(1, 2), False)
print(shared_bits(16, 8), False)
print(shared_bits(1, 1), False)
print(shared_bits(2, 3), False)
print(shared_bits(7, 10), False)
print(shared_bits(43, 77), True)
print(shared_bits(7, 15), True)
print(shared_bits(23, 7), True)
