# 7 kyu
# Exclamation marks series #7: Remove words from the sentence if it contains one exclamation mark


def remove(s):
    s_copy = s[:]
    s = s.split()
    lst = []

    for i in s:
        lst.append(i.count('H') + i.count('i') + i.count('!'))

    lst = [i % 3 for i in lst]

    if list(set(lst)) == [0]:
        return ''
    return s_copy


print(remove('Hi!'), '')
print(remove('Hi!!!'), 'Hi!!!')
print(remove('!Hi'), '')
print(remove('!Hi!'), '!Hi!')
print(remove('Hi! Hi!'), '')
print(remove('!!!Hi !!hi!!! !hi'), '!!!Hi !!hi!!!')
print(remove('!Hi! ! !Hi!'), '!Hi! !Hi!')
