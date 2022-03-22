# 7 kyu
# Thinking & Testing : Something capitalized


def testit(s):
    s = s.split()
    return ' '.join(i[:-1] + i[-1].upper() for i in s)


print(testit(""), "")
print(testit("a"), "A")
print(testit("b"), "B")
print(testit("a a"), "A A")
print(testit("a b"), "A B")
print(testit("a b c"), "A B C")
print(testit("AA"), "aA")
print(testit("'fukv zsor tjss'"), 'fukV zsoR tjsS')
