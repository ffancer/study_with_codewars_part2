# 7 kyu
# Exclamation marks series #8: Move all exclamation marks to the end of the sentence


def remove(s):
    cnt = 0
    for i in s[::-1].lstrip('!'):
        if i == '!':
            cnt += 1

    # s.strip()[:-1].replace('!', '')
    return s.strip()[:-1].replace('!', '')
    # return s + '!' * cnt


print(remove("Hi!"), "Hi!")
print(remove("Hi! Hi!"), "Hi Hi!!")
print(remove("Hi! Hi! Hi!"), "Hi Hi Hi!!!")
print(remove("Hi! !Hi Hi!"), "Hi Hi Hi!!!")
print(remove("Hi! Hi!! Hi!"), "Hi Hi Hi!!!!")