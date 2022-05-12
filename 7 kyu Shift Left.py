def shift_left(a, b):
    r = len(a) + len(b)
    for i in range(-1, -min(len(a), len(b)) - 1, -1):
        if a[i] != b[i]:
            break
        r -= 2
    return r

print(shift_left("test", "west"), 2)
print(shift_left("test", "yes"), 7)
print(shift_left("b", "ab"), 1)
