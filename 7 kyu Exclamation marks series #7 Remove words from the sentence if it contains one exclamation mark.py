# 7 kyu
# Exclamation marks series #7: Remove words from the sentence if it contains one exclamation mark


def remove(s):
    pass


print(remove('Hi!'), '')
print(remove('Hi!!!'), 'Hi!!!')
print(remove('!Hi'), '')
print(remove('!Hi!'), '!Hi!')
print(remove('Hi! Hi!'), '')
print(remove('!!!Hi !!hi!!! !hi'), '!!!Hi !!hi!!!')
print(remove('!Hi! ! !Hi!'), '!Hi! !Hi!')
