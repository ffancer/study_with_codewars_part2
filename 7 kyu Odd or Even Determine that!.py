# 7 kyu
# Odd or Even? Determine that!


def odd_or_even(n):
    if n % 2 == 1:
        return 'Either'
    elif (n / 2) % 2 == 0:
        return 'Even'
    return 'Odd'

print(odd_or_even(1), "Either")
print(odd_or_even(3), "Either")
print(odd_or_even(6), "Odd")
print(odd_or_even(8), "Even")
