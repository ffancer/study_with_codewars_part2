def first_non_repeated(s):
    for i in s:
        if s.count(i) == 1:
            return i
    return s[0]


print(first_non_repeated("test"), 'e')
print(first_non_repeated("teeter"), 'r')
print(first_non_repeated("1122321235121222"), '5')
