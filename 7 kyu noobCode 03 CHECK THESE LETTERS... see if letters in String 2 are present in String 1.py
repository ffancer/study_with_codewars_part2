# 7 kyu
# noobCode 03: CHECK THESE LETTERS... see if letters in "String 2" are present in "String 1"


def letter_check(arr):
    # your code here
    pass


print(letter_check(["abcd", "aaa"]), True)
print(letter_check(["trances", "nectar"]), True)
print(letter_check(["THE EYES", "they see"]), True)
print(letter_check(["assert", "staring"]), False)
print(letter_check(["arches", "later"]), False)
print(letter_check(["dale", "caller"]), False)
print(letter_check(["parses", "parsecs"]), False)
print(letter_check(["replays", "adam"]), False)
print(letter_check(["mastering", "streaming"]), True)
print(letter_check(["drapes", "compadres"]), False)
print(letter_check(["deltas", "slated"]), True)
print(letter_check(["deltas", ""]), True)
print(letter_check(["", "slated"]), False)
