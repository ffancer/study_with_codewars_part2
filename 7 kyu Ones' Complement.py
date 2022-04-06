def ones_complement(binary_number):
    return ''.join('0' if i == '1' else '1' for i in binary_number)


print(ones_complement("0"), "1")
print(ones_complement("1"), "0")
print(ones_complement("01"), "10")
print(ones_complement("10"), "01")
print(ones_complement("1101"), "0010")
