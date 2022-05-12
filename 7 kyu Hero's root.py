def int_rac(n, guess):
    # return (n + guess / n) / 2
    x = (guess + n / guess) / 2
    if abs(x - guess) < 1:
        return 1

print(int_rac(25, 1), 4)
print(int_rac(125348, 300), 3)
