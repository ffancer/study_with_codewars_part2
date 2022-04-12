# 7 kyu
# Exclamation marks series #7: Remove words from the sentence if it contains one exclamation mark


def remove(s):
    s = s.split()
    lst = []
    for i in s:
        lst.append(i.count('H') + i.count('i') + i.count('!'))
    return lst


print(remove('Hi!'), '')
print(remove('Hi!!!'), 'Hi!!!')
print(remove('!Hi'), '')
print(remove('!Hi!'), '!Hi!')
print(remove('Hi! Hi!'), '')
print(remove('!!!Hi !!hi!!! !hi'), '!!!Hi !!hi!!!')
print(remove('!Hi! ! !Hi!'), '!Hi! !Hi!')
