def solve(nums, div):
    return [i % div + i for i in nums]


print(solve([2, 7, 5, 9, 100, 34, 32, 0], 3), [4, 8, 7, 9, 101, 35, 34, 0])
print(solve([1000, 999, 998, 997], 5), [1000, 1003, 1001, 999])
print(solve([], 2), [])
