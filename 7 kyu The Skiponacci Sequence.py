def skiponacci(n):
    fib1, fib2 = 1, 1
    s = ''
    i = 0
    while i < n - 2:
        fib_sum = fib1 + fib2
        fib1 = fib2
        fib2 = fib_sum
        i = i + 1
        s += str(fib2) + ' '
    return s


print(skiponacci(1), "1")
print(skiponacci(5), "1 skip 2 skip 5")
print(skiponacci(7), "1 skip 2 skip 5 skip 13")
