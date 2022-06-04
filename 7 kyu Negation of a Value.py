def negation_value(s, val):
    return len(s) % 2 ^ bool(val)


print(negation_value("!", False), True)
print(negation_value("!", True), False)
print(negation_value("!!!", []), True)
