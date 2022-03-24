def without_last(lst):
    # Fix it
    lst.pop()  # removes the last element
    return lst


print(without_last([1, 2, 3, 4, 5]), [1, 2, 3, 4])
print(without_last([9, 7, 6, 9]), [9, 7, 6])
