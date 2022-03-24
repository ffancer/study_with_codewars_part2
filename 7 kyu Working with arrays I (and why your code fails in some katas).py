def without_last(lst):
    lst_copy = list(lst) # creates a shallow copy
    lst_copy.pop()
    return lst_copy

# There are several other ways to solve this
# like returning lst[:-1] directly or creating a new list iteratively with all the elements of lst minus the last one


print(without_last([1, 2, 3, 4, 5]), [1, 2, 3, 4])
print(without_last([9, 7, 6, 9]), [9, 7, 6])
