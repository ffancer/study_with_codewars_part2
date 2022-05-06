# 7 kyu
# isEven? - Bitwise Series


def is_even(n):
    return str(n / 2)[-1] == '0'


print(is_even(2), True, "Expected 'True'")
print(is_even(3), False, "Expected 'False'")
print(is_even(14), True, "Expected 'True'")
print(is_even(15), False, "Expected 'False'")
print(is_even(26), True, "Expected 'True'")
print(is_even(27), False, "Expected 'False'")
