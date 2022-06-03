# 7 kyu
# Are there doubles?


def double_check(strng):
    return ''.join(list(set(strng)))


print(double_check("abca"), False)
print(double_check("aabc"), True)
print(double_check("a 11 c d"), True)
print(double_check("AabBcC"), True)
print(double_check("a b  c"), True)
print(double_check("a b c d e f g h i h k"), False)
