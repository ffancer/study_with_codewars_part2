def transpose_two_strings(arr):
    first, second = arr[0], arr[1]
    s = ''

    for i in range(max(len(first), len(second))):
        s +=


print(transpose_two_strings(["Hello", "World"]), "H W\ne o\nl r\nl l\no d")
print(transpose_two_strings(["joey", "louise"]), "j l\no o\ne u\ny i\n  s\n  e")
print(transpose_two_strings(["a", "cat"]), "a c\n  a\n  t")
print(transpose_two_strings(["cat", ""]), "c  \na  \nt  ")
print(transpose_two_strings(["!a!a!", "?b?b"]), "! ?\na b\n! ?\na b\n!  ")
