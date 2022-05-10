def mispelled(word1, word2):
    return sorted(list(set(word1)))


print(mispelled('versed', 'xersed'), True)
print(mispelled('versed', 'applb'), False)
print(mispelled('versed', 'v5rsed'), True)
print(mispelled('1versed', 'versed'), True)
print(mispelled('versed', 'versed'), True)
