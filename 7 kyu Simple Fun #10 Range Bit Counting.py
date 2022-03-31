# 7 kyu
# Simple Fun #10: Range Bit Counting


def range_bit_count(a, b):
    return ''.join([bin(i)[2:] for i in range(a, b+1)]).count('1')


print(range_bit_count(2, 7), 11)
print(range_bit_count(0, 1), 1)
print(range_bit_count(4, 4), 1)
