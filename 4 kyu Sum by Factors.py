def prime_factors(n):
    lst = []
    n = abs(n)
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n /= i
            lst.append(i)
    if n > 1:
        lst.append(n)
    return lst


def combine(lst_1, lst_2):
    for i in lst_1:
        if not i in lst_2:
            lst_2.append(i)
    return lst_2


def sum_for_list(lst):
    factors = []
    total = []

    for i in range(len(lst)):
        combine(prime_factors(lst[i]), factors)
    for i in range(len(factors)):
        cnt = 0
        for j in range(len(lst)):
            if not lst[j] % factors[i]:
                cnt += lst[j]
        total.append([factors[i], cnt])
    total.sort(key=lambda x: x[0])
    return total


a = [12, 15]
print(sum_for_list(a), [[2, 12], [3, 27], [5, 15]])

a = [15, 21, 24, 30, 45]
print(sum_for_list(a), [[2, 54], [3, 135], [5, 90], [7, 21]])
