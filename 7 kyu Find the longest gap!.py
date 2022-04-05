def gap(num):
    # cnt, biggest_zero = 1, 0
    # i = 0
    # num = bin(num)[2:]
    # while i < len(num)-1:
    #     if num[i] == num[i+1] == '0':
    #         cnt += 1
    #
    #     biggest_zero = cnt
    #     cnt = 0
    #     i += 1
    # return biggest_zero
    return bin(num)[2:].split('1')


print(gap(9), 2)
print(gap(529), 4)
print(gap(20), 1)
print(gap(15), 0)
