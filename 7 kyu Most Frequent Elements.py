def find_most_frequent(l):
    return set(x for x in set(l) if l.count(x) == max([l.count(y) for y in l]))


print(find_most_frequent([1, 1, 2, 3]), set([1]), 'one most frequent element')
print(find_most_frequent([1, 1, 2, 2, 3]), set([1, 2]), 'two most frequent element')
print(find_most_frequent([]), set([]), 'empty')
