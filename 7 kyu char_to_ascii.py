def char_to_ascii(s):
    pass


print(char_to_ascii(""), None, "deals with an empty string")
print(char_to_ascii("a"), {"a": 97}, "deals with one char")
print(char_to_ascii("aaa"), {"a": 97}, "deals with repeated characters")
print(char_to_ascii("hello world"), {"h": 104, "e": 101, "l": 108, "o": 111, "w": 119, "r": 114, "d": 100},
                   "deals with spaces")
print(char_to_ascii("ABaa ^"), {"A": 65, "B": 66, "a": 97},
                   "deals with uppercase characters and non alphebetic characters")
