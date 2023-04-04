def keep_order(ary, val):
    for i, j in enumerate(ary):
        # if j < val < j[i + 1]:
        #     return val
        print(i+1)
    return 'gg'


print(keep_order([1, 2, 3, 4, 7], 5), 4, "Testing keep_order([1, 2, 3, 4, 7], 5)")
print(keep_order([1, 2, 3, 4, 7], 0), 0, "Testing keep_order([1, 2, 3, 4, 7], 0)")
print(keep_order([1, 1, 2, 2, 2], 2), 2, "Testing keep_order([1, 1, 2, 2, 2], 2)")
print(keep_order([1, 2, 3, 4], 5), 4, "Testing keep_order([1, 2, 3, 4], 5)")
print(keep_order([1, 2, 3, 4], -1), 0, "Testing keep_order([1, 2, 3, 4], -1)")
print(keep_order([1, 2, 3, 4], 2), 1, "Testing keep_order([1, 2, 3, 4], 2)")
print(keep_order([1, 2, 3, 4], 0), 0, "Testing keep_order([1, 2, 3, 4], 0)")
print(keep_order([1, 2, 3, 4], 1), 0, "Testing keep_order([1, 2, 3, 4], 1)")
print(keep_order([1, 2, 3, 4], 2), 1, "Testing keep_order([1, 2, 3, 4], 2)")
print(keep_order([1, 2, 3, 4], 3), 2, "Testing keep_order([1, 2, 3, 4], 3)")
