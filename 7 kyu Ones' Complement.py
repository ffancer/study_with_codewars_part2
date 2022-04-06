def ones_complement(binary_number):
    ans = ''

    for i in binary_number:
        if i == '1':
            ans += '0'
        else:
            ans += '1'

    return ans


print(ones_complement("0"), "1")
print(ones_complement("1"), "0")
print(ones_complement("01"), "10")
print(ones_complement("10"), "01")
print(ones_complement("1101"), "0010")
