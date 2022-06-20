# 3 kyu
# How many are smaller than me II?


def smaller(arr):
    cnt = 0
    lst = []
    i, j = 0, 1

    while arr:
        while j < len(arr):
            if arr[i] > arr[j]:
                cnt += 1
                j += 1
            # elif arr[i] < arr[j]:
            #     j += 1
            # elif arr[i] == arr[j]:
            #     j += 1
            else:
                j += 1
        lst.append(cnt)
        cnt = 0
        arr = arr[1:]
        j = 1


    return lst


# print(smaller([5, 4, 3, 2, 1]), [4, 3, 2, 1, 0])
# print(smaller([1, 2, 3]), [0, 0, 0])
# print(smaller([1, 2, 0]), [1, 1, 0])
print(smaller([1, 2, 1]), [0, 1, 0])
print(smaller([1, 1, -1, 0, 0]), [3, 3, 0, 0, 0])
print(smaller([5, 4, 7, 9, 2, 4, 4, 5, 6]), [4, 1, 5, 5, 0, 0, 0, 0, 0])
print(smaller([5, 4, 7, 9, 2, 4, 1, 4, 5, 6]), [5, 2, 6, 6, 1, 1, 0, 0, 0, 0])
