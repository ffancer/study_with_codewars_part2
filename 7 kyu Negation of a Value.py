def negation_value(s, val):
    if not s:
        return bool(val)

    while s:
        val = not val
        s = s[1:]

    return val


print(negation_value("!", False), True)
print(negation_value("!", True), False)
print(negation_value("!!!", []), True)
