# 7 kyu
# Exclamation marks series #8: Move all exclamation marks to the end of the sentence


def remove(s):
    cnt = 0
    return s.split()


print(remove("Hi!"), "Hi!")
print(remove("Hi! Hi!"), "Hi Hi!!")
print(remove("Hi! Hi! Hi!"), "Hi Hi Hi!!!")
print(remove("Hi! !Hi Hi!"), "Hi Hi Hi!!!")
print(remove("Hi! Hi!! Hi!"), "Hi Hi Hi!!!!")