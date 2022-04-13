def perfect_roots(n):
    i,j = 1, 1
    while i != n:
        i=** j
        if i < n:
            j += 1
    return i, j


print(perfect_roots(256), True)
print(perfect_roots(1000), False)
print(perfect_roots(6561), True)
