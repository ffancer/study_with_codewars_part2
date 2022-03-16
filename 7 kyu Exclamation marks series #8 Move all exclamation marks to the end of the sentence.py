# 7 kyu
# Exclamation marks series #8: Move all exclamation marks to the end of the sentence


def remove(s):
    cnt = 0

    for i in s.split()[:-1]:
        if '!' in i:
            cnt += 1

    return cnt


print(remove("Hi!"), "Hi!")
print(remove("Hi! Hi!"), "Hi Hi!!")
print(remove("Hi! Hi! Hi!"), "Hi Hi Hi!!!")
print(remove("Hi! !Hi Hi!"), "Hi Hi Hi!!!")
print(remove("Hi! Hi!! Hi!"), "Hi Hi Hi!!!!")