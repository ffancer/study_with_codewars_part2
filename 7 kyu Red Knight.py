def red_knight(N, P):
    ans = 'Black'

    if (P - N) % 2 == 0:
        ans = 'White'

    return ans, P * 2


print(red_knight(0, 8), ('White', 16))
print(red_knight(0, 7), ('Black', 14))
print(red_knight(1, 6), ('Black', 12))
print(red_knight(1, 5), ('White', 10))
