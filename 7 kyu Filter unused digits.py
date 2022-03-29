def unused_digits(*args):
    ten_digits = '0123456789'
    digits = ''.join(str(i) for i in args)
    return digits

print(unused_digits(12, 34, 56, 78), "09")
print(unused_digits(2015, 8, 26), "3479")
print(unused_digits(276, 575), "013489")
print(unused_digits(643), "0125789")
print(unused_digits(864, 896, 744), "01235")
