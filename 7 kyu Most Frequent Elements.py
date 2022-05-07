def find_most_frequent(l):
    dct = {}

    for i in l:
        dct.update({i: l.count(i)})

    return dct


print(find_most_frequent([1, 1, 2, 3]), set([1]), 'one most frequent element')
print(find_most_frequent([1, 1, 2, 2, 3]), set([1, 2]), 'two most frequent element')
print(find_most_frequent([]), set([]), 'empty')
