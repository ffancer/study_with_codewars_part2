def fibonacci_of(num):
    if num in {0, 1}:
        return num
    return fibonacci_of(num - 1) + fibonacci_of(num - 2)



def perimeter(n):
    return sum(fibonacci_of(i) for i in range(1, n+1)) * 4


print(perimeter(5), 80)
print(perimeter(7), 216)
print(perimeter(20), 114624)
print(perimeter(30), 14098308)
print(perimeter(100), 6002082144827584333104)
