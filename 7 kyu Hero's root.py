def int_rac(n, guess):
    # return (n + guess / n) / 2
    cnt = 0
    while n > 0:
        cnt += 1
        n = (n + guess / n) / 2
    return cnt

print(int_rac(25, 1), 4)
print(int_rac(125348, 300), 3)
