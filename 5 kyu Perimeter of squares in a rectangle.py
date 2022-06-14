def perimeter(n):
    fib = [1, 1]

    for i in range(2, n + 1):
        fib.append(fib[i-1] + fib[i-2])

    return sum(fib) * 4


print(perimeter(5), 80)
print(perimeter(7), 216)
print(perimeter(20), 114624)
print(perimeter(30), 14098308)
print(perimeter(100), 6002082144827584333104)
