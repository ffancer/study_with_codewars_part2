# 7 kyu
# Odd or Even? Determine that!


def odd_or_even(n):
    return 'Either' if n % 2 == 1 else 'Even' if (n / 2) % 2 == 0 else 'Odd'


print(odd_or_even(1), "Either")
print(odd_or_even(3), "Either")
print(odd_or_even(6), "Odd")
print(odd_or_even(8), "Even")
