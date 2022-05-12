def fit_in(a, b, m, n):
    return a + b <= max(m, n) or max(a, b) <= min(m, n)


print(fit_in(1, 2, 3, 2), True)
print(fit_in(1, 2, 2, 1), False)
print(fit_in(3, 2, 3, 2), False)
print(fit_in(1, 2, 1, 2), False)
