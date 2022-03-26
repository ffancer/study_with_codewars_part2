def womens_age(n):
    base = n // 2 if n % 2 == 0 else (n - 1) // 2
    new_n = 20 if n % 2 == 0 else 21
    return f"{n}? That's just {new_n}, in base {base}!"


print(womens_age(32), "32? That's just 20, in base 16!")
print(womens_age(39), "39? That's just 21, in base 19!")
