def password(string):
    cnt = 0

    if len(string) == 8:
        cnt += 1

    for i in string:
        if i.isupper():
            cnt += 1
        elif i.islower():
            cnt += 1
        elif i.isdigit():
            cnt += 1

    return cnt >= 4


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
