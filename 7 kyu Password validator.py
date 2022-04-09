def password(string):
    cnt_upper, cnt_lower, cnt_digit = 0, 0, 0

    if len(string) < 8:
        return False

    for i in string:
        if i.isupper():
            cnt_upper += 1
        elif i.islower():
            cnt_lower += 1
        elif i.isdigit():
            cnt_digit += 1

    return cnt


print(password("Abcd1234"), True)
print(password("Abcd123"), False)
print(password("abcd1234"), False)
print(password("AbcdefGhijKlmnopQRsTuvwxyZ1234567890"), True)
print(password("ABCD1234"), False)
print(password("Ab1!@#$%^&*()-_+={}[]|\:;?/>.<,"), True)
print(password("!@#$%^&*()-_+={}[]|\:;?/>.<,"), False)
print(password(""), False)
print(password(" aA1----"), True)
print(password("4aA1----"), True)
