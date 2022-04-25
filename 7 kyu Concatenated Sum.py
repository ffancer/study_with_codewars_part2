def check_concatenated_sum(num, n):
    lst = []
    for i in str(num):
        lst.append(int(i * n))
    return sum(lst) == num


print(check_concatenated_sum(2997, 3), True)
# print(check_concatenated_sum(-2997, 3), True)
