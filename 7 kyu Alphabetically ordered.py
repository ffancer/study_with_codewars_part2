def alphabetic(s):
    return list(s) == sorted(list(s))


print(alphabetic('asd'), False)
print(alphabetic('codewars'), False)
print(alphabetic('door'), True)
print(alphabetic('cell'), True)
print(alphabetic('z'), True)
print(alphabetic(''), True)
