import re

# s = 'fjd3IR9'
# match = re.match('\d', s)
#
# if match:
#     print(match)

valid = re.compile(r"^[a2-9tjqk]{5}$")
print(valid.match("akt5q"))

# regex = ""
#
# print(regex, 'fjd3IR9'), True
# print(bool(search(regex, 'ghdfj32')), False)
# print(bool(search(regex, 'DSJKHD23')), False)
# print(bool(search(regex, 'dsF43')), False)
# print(bool(search(regex, '4fdg5Fj3')), True)
# print(bool(search(regex, 'DHSJdhjsU')), False)
# print(bool(search(regex, 'fjd3IR9.;')), False)
# print(bool(search(regex, 'fjd3  IR9')), False)
# print(bool(search(regex, 'djI38D55')), True)
# print(bool(search(regex, 'a2.d412')), False)
# print(bool(search(regex, 'JHD5FJ53')), False)
# print(bool(search(regex, '!fdjn345')), False)
# print(bool(search(regex, 'jfkdfj3j')), False)
# print(bool(search(regex, '123')), False)
# print(bool(search(regex, 'abc')), False)
# print(bool(search(regex, '123abcABC')), True)
# print(bool(search(regex, 'ABC123abc')), True)
# print(bool(search(regex, 'Password123')), True)
