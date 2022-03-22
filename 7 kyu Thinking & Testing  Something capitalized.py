# 7 kyu
# Thinking & Testing : Something capitalized


def testit(s):
    s = s.split()

    if len(s[0]) == 2:
        return ' '.join(i[0].lower() + i[1] for i in s)


# print(testit(""), "")
# print(testit("a"), "A")
# print(testit("b"), "B")
# print(testit("a a"), "A A")
# print(testit("a b"), "A B")
# print(testit("a b c"), "A B C")
print(testit("AA"), "aA")

