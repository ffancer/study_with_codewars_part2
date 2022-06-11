def fold_array(arr, runs):
    for _ in range(runs):
        mid_len = len(arr) // 2
        lst = [arr[i] + arr[-1-i] for i in range(mid_len)] + [arr[mid_len]]*(len(arr)%2)
        arr = lst.copy()
    return arr



arr = [1, 2, 3, 4, 5]

tests = [
    [[arr, 1], [6, 6, 3]],
    [[arr, 2], [9, 6]],
    [[arr, 3], [15]],
    [[[-9, 9, -8, 8, 66, 23], 1], [14, 75, 0]],
]

for inp, exp in tests:
    print(fold_array(*inp), exp)
