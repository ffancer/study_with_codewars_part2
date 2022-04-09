# 7 kyu
# Simple Fun #20: First Reverse Try

def first_reverse_try(arr):
    if not arr or len(arr) == 1:
        return arr
    return [arr[-1]] + arr[1:-1] + [arr[0]]


print(first_reverse_try([1, 2, 3, 4, 5]), [5, 2, 3, 4, 1])
print(first_reverse_try([3, 5, 6, 2]), [2, 5, 6, 3])
print(first_reverse_try([]), [])
print(first_reverse_try([111]), [111])
