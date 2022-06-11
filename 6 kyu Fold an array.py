def fold_array(array, runs):
    nums = list(array)
    for _ in range(runs):
        for a in range(len(nums) // 2):
            nums[a] += nums.pop()
    return nums


arr = [1, 2, 3, 4, 5]

tests = [
    [[arr, 1], [6, 6, 3]],
    [[arr, 2], [9, 6]],
    [[arr, 3], [15]],
    [[[-9, 9, -8, 8, 66, 23], 1], [14, 75, 0]],
]

for inp, exp in tests:
    print(fold_array(*inp), exp)
