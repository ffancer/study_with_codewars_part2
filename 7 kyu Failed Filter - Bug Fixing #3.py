def filter_numbers(string):
    return "".join(x for x in string if int(x))


print(filter_numbers("test123"), 'test', 'Just return the string')
print(filter_numbers("a1b2c3"), 'abc', 'Just return the string')
print(filter_numbers("aa1bb2cc3dd"), 'aabbccdd', 'Just return the string')
