# def perimeter(n):
#     pass


def fibonacci_of(n):
    if n in {0, 1}:
        return n
    return fibonacci_of(n - 1) + fibonacci_of(n - 2)


print([fibonacci_of(i) for i in range(1, 7)])
# print(perimeter(5), 80)
# print(perimeter(7), 216)
# print(perimeter(20), 114624)
# print(perimeter(30), 14098308)
# print(perimeter(100), 6002082144827584333104)
