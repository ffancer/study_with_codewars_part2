# 7 kyu
# 99 Problems, #1: last in list


def last(lst):
    if not lst:
        return None
    return lst[-1]


print(last([1, 2, 3]), 3, "last([1,2,3]) == 3")
print(last([]), None, "last( [] ) == None")
