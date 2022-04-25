def check_concatenated_sum(num, n):
    lst = []

    for i in str(abs(num)):
        lst.append(i * n)
    lst = list(map(int, lst))

    return sum(lst) == abs(num)


print(check_concatenated_sum(2997, 3), True)
print(check_concatenated_sum(-2997, 3), True)
