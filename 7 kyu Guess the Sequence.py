def sequence(x):
    return sorted(range(1,x+1), key=str)


print(sequence(16), [1, 10, 11, 12, 13, 14, 15, 16, 2, 3, 4, 5, 6, 7, 8, 9])
print(sequence(9), [1, 2, 3, 4, 5, 6, 7, 8, 9])
