# 3 kyu
# How many are smaller than me II?


# def smaller(arr):
#     sort_nums = sorted(arr)
#     dct = {}
#     lst = []
#
#     for i in range(len(sort_nums)):
#         if sort_nums[i] not in dct:
#             dct[sort_nums[i]] = i
#     for i in arr:
#         lst.append(dct[i])
#     return lst




# def smaller(arr):
#     lst = []
#     dct = {}
#
#     for i in range(len(arr)):
#         if arr[i] not in dct:
#             dct[arr[i]] = i
#     return dct
#
#
#
# print(smaller([5, 4, 3, 2, 1]), [4, 3, 2, 1, 0])
# print(smaller([1, 2, 3]), [0, 0, 0])
# print(smaller([1, 2, 0]), [1, 1, 0])
# print(smaller([1, 2, 1]), [0, 1, 0])
# print(smaller([1, 1, -1, 0, 0]), [3, 3, 0, 0, 0])
# print(smaller([5, 4, 7, 9, 2, 4, 4, 5, 6]), [4, 1, 5, 5, 0, 0, 0, 0, 0])
# print(smaller([5, 4, 7, 9, 2, 4, 1, 4, 5, 6]), [5, 2, 6, 6, 1, 1, 0, 0, 0, 0])

# lst = [5, 4, 3, 2, 1]
# num = 5
# more = 0
# less = 0
# for i in lst:
#       if i < num: less += 1
#       if i > num: more += 1
# print(more, less)


# def smaller(arr):
#     cnt = 0
#     lst = []
#     while arr:
#         for j in arr:
#             target = arr[0]
#             if target > j:
#                 cnt += 1
#         arr = arr[1:]
#         lst.append(cnt)
#         cnt = 0
#     return lst




def smaller(arr):
    lst = []
    cnt = 0

    while arr:
        x = arr.pop(0)
        for i in arr:
            if x > i:
                cnt += 1
        lst.append(cnt)
        cnt = 0

    return lst


print(smaller([5, 4, 3, 2, 1]), [4, 3, 2, 1, 0])
print(smaller([5, 4, 7, 9, 2, 4, 1, 4, 5, 6]), [5, 2, 6, 6, 1, 1, 0, 0, 0, 0])
print(smaller([1, 2, 3]), [0, 0, 0])


# list(filter(lambda x: x % 2 == 1, [10, 111, 102, 213, 314, 515]))


# a = filter(lambda x: max(lst), lst)
# print(a)


# def smaller(xs):
#     # prepare list "ys" containing item's numeric order
#     ys = sorted((x,i) for i,x in enumerate(xs))
#     zs = [0] * len(ys)
#
#     for i in range(1, len(ys)):
#         zs[ys[i][1]] = zs[ys[i-1][1]]
#         if ys[i][0] != ys[i-1][0]: zs[ys[i][1]] += 1
#
#     # use list "ts" as binary search tree, every element keeps count of
#     # number of children with value less than the current element's value
#     ts = [0] * (zs[ys[-1][1]]+1)
#     us = [0] * len(xs)
#
#     for i in range(len(xs)-1,-1,-1):
#         x = zs[i]+1
#         while True:
#             us[i] += ts[x-1]
#             x -= (x & (-x))
#             if x <= 0: break
#
#         x = zs[i]+1
#         while True:
#             x += (x & (-x))
#             if x > len(ts): break
#             ts[x-1] += 1
#
#     return us

# print(smaller([5, 4, 3, 2, 1]), [4, 3, 2, 1, 0])
# print(smaller([40, 20, 10, 50, 20, 40, 30]), [4, 3, 2, 1, 0])