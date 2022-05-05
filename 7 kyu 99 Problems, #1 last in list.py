# 7 kyu
# 99 Problems, #1: last in list


def last(lst):
    return None if not lst else lst[-1]


print(last([1, 2, 3]), 3, "last([1,2,3]) == 3")
print(last([]), None, "last( [] ) == None")
