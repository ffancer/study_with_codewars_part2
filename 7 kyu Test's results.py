def test(r):
    average_mark = round(sum(r) / len(r), 3)
    lst1 = ['h', 'a', 'l']
    h = r.count(10) + r.count(9)
    a = r.count(8) + r.count(7)
    l = r.count(6) + r.count(5) + r.count(4) + r.count(3) + r.count(2) + r.count(1)
    lst2 = [h, a, l]
    dct = dict(zip(lst1, lst2))

    if a == 0 and l == 0:
        return [average_mark, dct, 'They did well']
    return [average_mark, dct]


print(test([10, 9, 9, 10, 9, 10, 9]), [9.429, {'h': 7, 'a': 0, 'l': 0}, 'They did well'])
print(test([5, 6, 4, 8, 9, 8, 9, 10, 10, 10]), [7.9, {'h': 5, 'a': 2, 'l': 3}])
print(test([5, 6, 5, 7, 4, 5, 6, 6, 5]), [5.444, {'h': 0, 'a': 1, 'l': 8}])
print(test([9, 8, 7, 6, 9, 8, 10, 7, 6]), [7.778, {'h': 3, 'a': 4, 'l': 2}])
print(test([9, 10, 10, 10, 10, 10, 8, 9, 7, 8, 10]), [9.182, {'h': 8, 'a': 3, 'l': 0}])
print(test([3, 5, 6, 10, 8, 4, 10, 9]), [6.875, {'h': 3, 'a': 1, 'l': 4}])
print(test([10, 9, 9, 10, 9, 10]), [9.5, {'h': 6, 'a': 0, 'l': 0}, 'They did well'])
print(test([7, 6, 8, 9, 6, 7, 5, 9]), [7.125, {'h': 2, 'a': 3, 'l': 3}])
print(test([9, 9, 8, 9, 8, 9]), [8.667, {'h': 4, 'a': 2, 'l': 0}])
print(test([10, 9, 6, 7, 10, 8, 9, 10]), [8.625, {'h': 5, 'a': 2, 'l': 1}])
