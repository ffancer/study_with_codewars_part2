def perimeter(n):
    fibo = [1, 1]

    for i in range(2, n + 1):
        fibo.append(fibo[i-1] + fibo[i-2])

    return fibo


print(perimeter(5), 80)
print(perimeter(7), 216)
print(perimeter(20), 114624)
print(perimeter(30), 14098308)
print(perimeter(100), 6002082144827584333104)
