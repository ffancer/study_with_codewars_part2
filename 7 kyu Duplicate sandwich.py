def duplicate_sandwich(arr):
    border1, border2 = [i for i, j in enumerate(arr) if arr.count(j) == 2]
    return arr[border1 + 1: border2]


print(duplicate_sandwich([0, 1, 2, 3, 4, 5, 6, 1, 7, 8]), [2, 3, 4, 5, 6])
print(duplicate_sandwich(['None', 'Hello', 'Example', 'hello', 'None', 'Extra']),
      ['Hello', 'Example', 'hello'])
print(duplicate_sandwich([0, 0]), [])
print(duplicate_sandwich([True, False, True]), [False])
print(duplicate_sandwich(['e', 'x', 'a', 'm', 'p', 'l', 'e']), ['x', 'a', 'm', 'p', 'l'])
