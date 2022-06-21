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


# def smaller(arr):
#     lst = []
#     while arr:
#         for i in arr:
#             target = arr[0]
#             if target > i:
#                 del arr[i]
#         lst.append(len(arr))
#         arr = arr[1:]
#     return lst
#
#
#
#
# print(smaller([5, 4, 3, 2, 1]), [4, 3, 2, 1, 0])
# print(smaller([5, 4, 7, 9, 2, 4, 1, 4, 5, 6]), [5, 2, 6, 6, 1, 1, 0, 0, 0, 0])
# print(smaller([1, 2, 3]), [0, 0, 0])


# list(filter(lambda x: x % 2 == 1, [10, 111, 102, 213, 314, 515]))
# lst = [5, 4, 7, 9, 2, 4, 1, 4, 5, 6]

# a = filter(lambda x: max(lst), lst)
# print(a)

# for i in lst:
#     if i < 5:
#         lst.remove(i)
# print(lst)

def smaller(arr):
    lst = []
    while arr:
        for i in arr:
            target = arr[0]
            if i > target:
                arr.remove(i)
        lst.append(len(arr))
        arr = arr[1:]
    return lst




print(smaller([5, 4, 3, 2, 1]), [4, 3, 2, 1, 0])