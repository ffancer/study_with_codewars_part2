# 7 kyu
# Thinking & Testing : Something capitalized


def testit(s):
    ans = ''

    for i in s:
        if i.islower():
            ans += i.upper()
        else:
            ans += i

    return ans


print(testit(""), "")
print(testit("a"), "A")
print(testit("b"), "B")
print(testit("a a"), "A A")
print(testit("a b"), "A B")
print(testit("a b c"), "A B C")
