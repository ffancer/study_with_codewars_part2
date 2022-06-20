# 3 kyu
# How many are smaller than me II?


def smaller(arr):
    cnt = 0
    lst = []
    i, j = 0, 1

    while arr:
        if arr[i] > arr[j]:
            cnt += 1
        j += 1
        if j == arr[len(arr) - 1]:
            i += 1
            j += 1
        arr = arr[1:]
        lst.append(cnt)
        cnt = 0

    return lst


print(smaller([5, 4, 3, 2, 1]), [4, 3, 2, 1, 0])
print(smaller([1, 2, 3]), [0, 0, 0])
print(smaller([1, 2, 0]), [1, 1, 0])
print(smaller([1, 2, 1]), [0, 1, 0])
print(smaller([1, 1, -1, 0, 0]), [3, 3, 0, 0, 0])
print(smaller([5, 4, 7, 9, 2, 4, 4, 5, 6]), [4, 1, 5, 5, 0, 0, 0, 0, 0])
print(smaller([5, 4, 7, 9, 2, 4, 1, 4, 5, 6]), [5, 2, 6, 6, 1, 1, 0, 0, 0, 0])
