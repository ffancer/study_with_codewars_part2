def length_of_sequence(arr, n):
    if arr.count(n) != 2:
        return 0

    cnt = []

    for i in range(len(arr)):
        if arr[i] == n:
            cnt.append(i)

    return cnt[1] - cnt[0] + 1


print(length_of_sequence([1, 1], 1), 2, 'Returns two when there are only two elements in the array')
print(length_of_sequence([1, 2, 3, 1], 1), 4,
      'Returns four for an array of length four and the number to be searched at the boundaries')
print(length_of_sequence([-7, 5, 0, 2, 9, 5], 10), 0, 'Returns zero if element is missing from the array')
print(length_of_sequence([-7, 5, 0, 2, 9, 5], 5), 5, 'Returns five')
print(length_of_sequence([-7, 6, 2, -7, 4], -7), 4, 'Returns four')
