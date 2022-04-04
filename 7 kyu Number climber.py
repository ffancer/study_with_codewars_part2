def climb(n):
    lst = []

    while n:
        lst.append(n)
        n //= 2

    return lst[::-1]


print(climb(13), [1, 3, 6, 13])
print(climb(10), [1, 2, 5, 10])
print(climb(1), [1])
