def sum_square_even_root_odd(nums):
    lst = []

    for i in nums:
        if i % 2 == 0:
            lst.append(i ** 2)
        else:
            lst.append(i ** .5)

    return lst

print(sum_square_even_root_odd([4, 5, 7, 8, 1, 2, 3, 0]), 91.61)
print(sum_square_even_root_odd([1, 14, 9, 8, 17, 21]), 272.71)
