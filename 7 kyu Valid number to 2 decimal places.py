def valid_number(n):
    return n.split('.')[-1].isdigit()



print(valid_number("0.00"), True)
print(valid_number(".00"), True)
print(valid_number("-.00"), True)
print(valid_number(".30"), True)
print(valid_number("0.40"), True)
print(valid_number("34443.33"), True)
print(valid_number(".0a"), False)
print(valid_number("1.00."), False)
print(valid_number(".+00"), False)
print(valid_number("w.00"), False)
print(valid_number("..00"), False)
print(valid_number("1,00"), False)
