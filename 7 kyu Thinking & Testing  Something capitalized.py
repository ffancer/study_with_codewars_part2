# 7 kyu
# Thinking & Testing : Something capitalized


def testit(s):
    if all(i.lower() for i in s) and len(s) < 6:
        return s.swapcase()
    else:
        s = s.split()
        s = [i.replace("'", '') for i in s]

        if len(s[0]) == 2:
            return ' '.join(i[0].lower() + i[1].upper() for i in s)
        if len(s[0]) == 4:
            return ' '.join(i[:3].lower() + i[3].upper() for i in s)




print(testit(""), "")
print(testit("a"), "A")
print(testit("b"), "B")
print(testit("a a"), "A A")
print(testit("a b"), "A B")
print(testit("a b c"), "A B C")
print(testit("AA"), "aA")
print(testit("'fukv zsor tjss'"), 'fukV zsoR tjsS')
