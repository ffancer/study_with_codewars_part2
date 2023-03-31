def describe_age(age):
    if age <= 12:
        return "You're a(n) kid"
    elif 13 <= age <= 17:
        return "You're a(n) teenager"
    elif 18 <= age <= 64:
        return "You're a(n) adult"
    else:
        return "You're a(n) elderly"
    # dct = {
    #     f'{age <= 12}': "You're a(n) kid",
    #     13 <= age <= 17: "You're a(n) teenager",
    #     18 <= age <= 64: "You're a(n) adult",
    #     age > 64: "You're a(n) elderly",
    #     9: 'good'
    # }
    # return dct.get(age)
    # # return dct[age]


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
