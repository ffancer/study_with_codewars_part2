def unused_digits(*args):
    return ''.join(i for i in '0123456789' if i not in ''.join(str(i) for i in args))

print(unused_digits(12, 34, 56, 78), "09")
print(unused_digits(2015, 8, 26), "3479")
print(unused_digits(276, 575), "013489")
print(unused_digits(643), "0125789")
print(unused_digits(864, 896, 744), "01235")
