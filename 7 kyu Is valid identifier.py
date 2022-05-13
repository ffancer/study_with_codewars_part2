# 7 kyu
# Is valid identifier?


def is_valid(idn):
    pass


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
