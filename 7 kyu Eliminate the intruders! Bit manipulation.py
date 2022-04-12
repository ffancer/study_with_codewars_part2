def eliminate_unset_bits(number):
    if number.count('1') < 1:
        return 0
    return int(number.replace('0', ''), 2)


print(eliminate_unset_bits("11010101010101"), 255)
print(eliminate_unset_bits("111"), 7)
print(eliminate_unset_bits("1000000"), 1)
print(eliminate_unset_bits("000"), 0)
