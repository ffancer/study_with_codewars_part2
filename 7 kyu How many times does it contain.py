# 7 kyu
# How many times does it contain?


def string_counter(string, char):
    return string.count(char)


print(string_counter("Hello world", "o"), 2)
print(string_counter("Wait isn't it supposed to be cynical?", "i"), 4)
print(string_counter("I'm gona be the best code warrior ever dad", "r"), 4)
print(string_counter("Do you like Harry Potter?", "?"), 1)
