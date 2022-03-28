def alphabetic(s):
    return sorted(s) == list(s)


def alphabetic(s):
    return s == ''.join(sorted(s))

print(alphabetic('asd'), False)
print(alphabetic('codewars'), False)
print(alphabetic('door'), True)
print(alphabetic('cell'), True)
print(alphabetic('z'), True)
print(alphabetic(''), True)
