def fibonacci(n):
    fib1, fib2 = 1, 1

    for i in range(2, n):
        fib1, fib2 = fib2, fib1 + fib2
    return fib2


print(fibonacci(0), 0)
print(fibonacci(1), 1)
print(fibonacci(2), 1)
print(fibonacci(3), 2)
print(fibonacci(4), 3)
print(fibonacci(5), 5)
print(fibonacci(6), 8)
print(fibonacci(34), 5702887)
print(fibonacci(299), 137347080577163115432025771710279131845700275212767467264610201)
