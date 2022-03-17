def pyramid(balls):
    ans, var = 0, 1

    while balls > 0:
        ans += 1
        var += 1
        balls -= var

    return ans

print(pyramid(1), 1)
print(pyramid(4), 2)
print(pyramid(20), 5)
print(pyramid(100), 13)
print(pyramid(2211), 66)
print(pyramid(9999), 140)
