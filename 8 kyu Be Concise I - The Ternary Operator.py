def describe_age(a):
    b = "You're a(n) "
    # return f"You're a(n) "+('kid'if{a<13}else"teenager"if{a<18}else"adult"if{a<65}else"elderly")
    return f"You're a(n) "+('kid'if{a<13}else"teenager"if{a<18}else"adult"if{a<65}else"elderly")


print(describe_age(9), "You're a(n) kid")
print(describe_age(10), "You're a(n) kid")
print(describe_age(11), "You're a(n) kid")
print(describe_age(12), "You're a(n) kid")
print(describe_age(13), "You're a(n) teenager")
print(describe_age(14), "You're a(n) teenager")
print(describe_age(15), "You're a(n) teenager")
print(describe_age(16), "You're a(n) teenager")
print(describe_age(17), "You're a(n) teenager")
print(describe_age(18), "You're a(n) adult")
print(describe_age(19), "You're a(n) adult")
print(describe_age(63), "You're a(n) adult")
print(describe_age(64), "You're a(n) adult")
print(describe_age(65), "You're a(n) elderly")
print(describe_age(66), "You're a(n) elderly")
print(describe_age(100), "You're a(n) elderly")
