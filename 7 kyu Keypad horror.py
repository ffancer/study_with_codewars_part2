def computer_to_phone(numbers):
    s = ''
    dct = {'1': '7', '2': '8', '3': '9', '7': '1', '8': '2', '9': '3'}

    for i in numbers:
        if i in dct.keys():
            s += dct[i]
        else:
            s += i

    return s


print(computer_to_phone("0789456123"), "0123456789")
print(computer_to_phone("000"), "000")
print(computer_to_phone("94561"), "34567")
