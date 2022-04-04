def int_diff(arr, n):
    res = 0

    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if i != j and abs(arr[i] - arr[j]) == n:
                res += 1

    return res


print(int_diff([1, 1, 5, 6, 9, 16, 27], 4), 3)
print(int_diff([1, 1, 3, 3], 2), 4)
