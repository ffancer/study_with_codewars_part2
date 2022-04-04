def climb(n):
    i = 0
    lst = []
    while i < n:
        if i % 2 == 0:
            i = i * 2 + 1
            lst.append(i)
        else:
            i *= 2
            lst.append(i)
        # i += 1
    return lst

print(climb(13), [1, 3, 6, 13])
print(climb(10), [1, 2, 5, 10])
print(climb(1), [1])
