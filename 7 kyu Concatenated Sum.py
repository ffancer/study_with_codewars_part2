def check_concatenated_sum(num, n):
    lst = []
    try:
        for i in str(abs(num)):
            lst.append(i * n)
        lst = list(map(int, lst))

        return sum(lst) == abs(num)
    except:
        return False


print(check_concatenated_sum(2997, 3), True)
print(check_concatenated_sum(-2997, 3), True)
