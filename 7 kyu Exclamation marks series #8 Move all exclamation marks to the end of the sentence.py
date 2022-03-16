# 7 kyu
# Exclamation marks series #8: Move all exclamation marks to the end of the sentence


def remove(s):
    clear_s = s.replace('!', '')

    return clear_s + '!' * (len(s) - len(clear_s))


print(remove("Hi!"), "Hi!")
print(remove("Hi! Hi!"), "Hi Hi!!")
print(remove("Hi! Hi! Hi!"), "Hi Hi Hi!!!")
print(remove("Hi! !Hi Hi!"), "Hi Hi Hi!!!")
print(remove("Hi! Hi!! Hi!"), "Hi Hi Hi!!!!")