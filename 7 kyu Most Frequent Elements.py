# def find_most_frequent(l):
#     dct = {}
#
#     for i in l:
#         dct.update({i: l.count(i)})
#
#     return dct

def find_most_frequent(l):
    counter = 0
    num = l[0]

    for i in l:
        curr_frequency = l.count(i)
        if (curr_frequency > counter):
            counter = curr_frequency
            num = i

    return num


print(find_most_frequent([1, 1, 2, 3]), set([1]), 'one most frequent element')
print(find_most_frequent([1, 1, 2, 2, 3]), set([1, 2]), 'two most frequent element')
print(find_most_frequent([]), set([]), 'empty')
