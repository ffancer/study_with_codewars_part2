def search(budget, prices):
    return ','.join(str(i) for i in sorted(i for i in prices if budget >= i))


print(search(3, [6, 1, 2, 9, 2]), "1,2,2")
print(search(14, [7, 3, 23, 9, 14, 20, 7]), "3,7,7,9,14")
print(search(0, [6, 1, 2, 9, 2]), "")
print(search(10, []), "")
print(search(24, [24, 0, 100, 2, 5]), "0,2,5,24")
