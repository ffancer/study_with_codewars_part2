# 7 kyu
# Exclamation marks series #7: Remove words from the sentence if it contains one exclamation mark


def remove(s):
    return ' '.join(i for i in s.split() if i.count('!') != 1)


print(remove('Hi!'), '')
print(remove('Hi!!!'), 'Hi!!!')
print(remove('!Hi'), '')
print(remove('!Hi!'), '!Hi!')
print(remove('Hi! Hi!'), '')
print(remove('!!!Hi !!hi!!! !hi'), '!!!Hi !!hi!!!')
print(remove('!Hi! ! !Hi!'), '!Hi! !Hi!')
