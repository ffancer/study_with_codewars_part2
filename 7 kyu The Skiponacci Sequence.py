def skiponacci(n):
    fib1, fib2, lst, i, ans = 1, 1, [1, 1], 0, []

    while i < n - 2:
        fib_sum = fib1 + fib2
        fib1 = fib2
        fib2 = fib_sum
        lst.append(fib2)
        i = i + 1

    for i, j in enumerate(lst):
        if i % 2 == 0:
            ans.append(j)
        else:
            ans.append('skip')

    return ' '.join(str(i) for i in ans)


print(skiponacci(1), "1")
print(skiponacci(5), "1 skip 2 skip 5")
print(skiponacci(7), "1 skip 2 skip 5 skip 13")
