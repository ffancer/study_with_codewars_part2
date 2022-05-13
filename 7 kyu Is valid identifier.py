# 7 kyu
# Is valid identifier?


import string


def is_valid(idn):
    return (idn[0] in string.ascii_letters or idn[0] in '_$') and all(
        i in set(string.ascii_letters + '_$' + '0123456789') for i in idn) if idn else False


print(is_valid("okay_ok1"), True, "Wrong result for 'okay_ok1'")
print(is_valid("$ok"), True, "Wrong result for '$ok'")
print(is_valid("___"), True, "Wrong result for '___'")
print(is_valid("str_STR"), True, "Wrong result for 'str_STR'")
print(is_valid("myIdentf"), True, "Wrong result for 'myIdentf'")
print(is_valid("1ok0okay"), False, "Wrong result for '1ok0okay'")
print(is_valid("!Ok"), False, "Wrong result for '!Ok'")
print(is_valid(""), False, "Wrong result for an empty string")
print(is_valid("str-str"), False, "Wrong result for 'str-str'")
print(is_valid("no no"), False, "Wrong result for 'no no'")
