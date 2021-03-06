def scramble(string, array):
    lst = ['_'] * len(string)

    for i, j in enumerate(string):
        lst[array[i]] = j

    return ''.join(lst)


print(scramble('abcd', [0, 3, 1, 2]), 'acdb', "Should return acdb")
print(scramble('sc301s', [4, 0, 3, 1, 5, 2]), "c0s3s1", "Should return c0s3s1")
print(scramble('bskl5', [2, 1, 4, 3, 0]), "5sblk", "Should return 5sblk")
