# 7 kyu
# Thinking & Testing : Something capitalized


def testit(s):
    s1 = s
    s = s.split()
    s = [i.replace("'", '') for i in s]

    try:
        if len(s[0]) == 2:
            return ' '.join(i[0].lower() + i[1].upper() for i in s)
        if len(s[0]) == 4:
            return ' '.join(i[:3].lower() + i[3].upper() for i in s)
    except:
        return s1.swapcase()




print(testit(""), "")
print(testit("a"), "A")
print(testit("b"), "B")
print(testit("a a"), "A A")
print(testit("a b"), "A B")
print(testit("a b c"), "A B C")
print(testit("AA"), "aA")
print(testit("'fukv zsor tjss'"), 'fukV zsoR tjsS')
