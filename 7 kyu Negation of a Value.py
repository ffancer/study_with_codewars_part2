def negation_value(s, val):
    if '!' in s and val is True:
        return False
    if '!' in s and val is False:
        return True



print(negation_value("!", False), True)
print(negation_value("!", True), False)
print(negation_value("!!!", []), True)
