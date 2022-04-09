def password(string):
    pass


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
