def duplicate_sandwich(arr):
    border = [i for i in arr if arr.count(i) == 2][0]
    return arr[arr.index(border)+1:]

print(duplicate_sandwich([0, 1, 2, 3, 4, 5, 6, 1, 7, 8]), [2, 3, 4, 5, 6])
print(duplicate_sandwich(['None', 'Hello', 'Example', 'hello', 'None', 'Extra']),
      ['Hello', 'Example', 'hello'])
print(duplicate_sandwich([0, 0]), [])
print(duplicate_sandwich([True, False, True]), [False])
print(duplicate_sandwich(['e', 'x', 'a', 'm', 'p', 'l', 'e']), ['x', 'a', 'm', 'p', 'l'])
