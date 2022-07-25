def sum_of_differences(arr):
    if not arr or len(arr) == 1:
        return 0

    arr = sorted(arr, reverse=True)
    i, j = 0, 1
    lst = []

    while j < len(arr):
        lst.append(arr[i] - arr[j])
        i += 1
        j += 1
    return sum(lst)


print(sum_of_differences([1, 2, 10]), 9)
print(sum_of_differences([-3, -2, -1]), 2)
print(sum_of_differences([1, 1, 1, 1, 1]), 0)
print(sum_of_differences([-17, 17]), 34)
print(sum_of_differences([]), 0)
print(sum_of_differences([0]), 0)
print(sum_of_differences([-1]), 0)
print(sum_of_differences([1]), 0)
