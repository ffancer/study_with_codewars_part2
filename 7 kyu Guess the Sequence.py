def sequence(x):
    return [int(i) for i in sorted([str(i) for i in range(1, x + 1)])]


print(sequence(16), [1, 10, 11, 12, 13, 14, 15, 16, 2, 3, 4, 5, 6, 7, 8, 9])
print(sequence(9), [1, 2, 3, 4, 5, 6, 7, 8, 9])
