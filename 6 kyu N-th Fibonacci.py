def fibonacci_of(n):
    if n in {0, 1}:
        return n
    return fibonacci_of(n - 1) + fibonacci_of(n - 2)


def nth_fib(n):
    return [fibonacci_of(n) for n in range(n)][n-1]


print(nth_fib(1), 0, "1-st Fibo")
print(nth_fib(2), 1, "2-nd Fibo")
print(nth_fib(3), 1, "3-rd Fibo")
print(nth_fib(4), 2, "4-th Fibo")
print(nth_fib(5), 3, "5-th Fibo")
print(nth_fib(6), 5, "6-th Fibo")
print(nth_fib(7), 8, "7-th Fibo")
