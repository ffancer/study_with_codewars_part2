def prime_factors(n):
    f = []
    n = abs(n)
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n /= i
            f.append(i)
    if n > 1:
        f.append(n)
    return f


def sum_for_list(lst):
    pass


a = [12, 15]
print(sum_for_list(a), [[2, 12], [3, 27], [5, 15]])

a = [15, 21, 24, 30, 45]
print(sum_for_list(a), [[2, 54], [3, 135], [5, 90], [7, 21]])
