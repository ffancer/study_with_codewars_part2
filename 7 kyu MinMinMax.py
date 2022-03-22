def minMinMax(arr):
    big, small = max(arr), min(arr)
    ans = small + 1

    for i in range(small+1, big+1, 1):
        if ans not in arr:
            break
        else:
            ans = i

    return [small, ans, big]


print(minMinMax([-1, 4, 5, -23, 24]), [-23, -22, 24])
print(minMinMax([1, 3, -3, -2, 8, -1]), [-3, 0, 8])
print(minMinMax([2, -4, 8, -5, 9, 7]), [-5, -3, 9])
