def is_it_a_num(s: str) -> str:
    tel_number = ''.join(i for i in s if i.isdigit())
    return tel_number if len(tel_number) == 11 and tel_number[0] == '0' else "Not a phone number"


print(is_it_a_num("S:)0207ERGQREG88349F82!efRF)"), "02078834982")
print(is_it_a_num("sjfniebienvr12312312312ehfWh"), "Not a phone number")
print(is_it_a_num("0192387415456"), "Not a phone number")
print(is_it_a_num("v   uf  f 0tt2eg qe0b 8rtyq4eyq564()(((((165"), "02084564165")
print(is_it_a_num("stop calling me no I have never been in an accident"), "Not a phone number")
