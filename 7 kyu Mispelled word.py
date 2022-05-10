import regex


def mispelled(word1, word2):
    return ~len(word1) + ~len(word2) != -3 and regex.fullmatch(r'(?:\L<word1>){1i+1d+1s<=1}', word2,
                                                               word1={word1}) is not None or ~len(word1) + ~len(
        word2) == -3


print(mispelled('versed', 'xersed'), True)
print(mispelled('versed', 'applb'), False)
print(mispelled('versed', 'v5rsed'), True)
print(mispelled('1versed', 'versed'), True)
print(mispelled('versed', 'versed'), True)
