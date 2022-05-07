def make_parts(arr, chunkSize):
    lst = []

    while arr:
        lst.append(arr[:chunkSize])
        arr = arr[chunkSize:]

    return lst


print(make_parts([1, 2, 3, 4, 5], 2), [[1, 2], [3, 4], [5]])
print(make_parts([1, 2, 3], 1), [[1], [2], [3]])
print(make_parts([1, 2, 3, 4, 5], 10), [[1, 2, 3, 4, 5]])
