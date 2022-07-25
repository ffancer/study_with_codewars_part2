# 8 kyu
# How much water do I need?


def how_much_water(L, X, N):
    return 'Too much clothes' if N > X * 2 else 'Not enough clothes' if N < X else L * 1.1 ** (N - X)


print(how_much_water(10, 10, 21), 'Too much clothes')
print(how_much_water(10, 10, 2), 'Not enough clothes')
print(how_much_water(10, 11, 20), 23.58)
print(how_much_water(50, 15, 29), 189.87)
