def number_to_pwr(number, p):
    total = 0
    ans = 1
    while p != 0:
        total = number * number
        ans /= total
        p -= 1

    return ans



# print(number_to_pwr(4, 2), 16)
print(number_to_pwr(10, 4), 10000)
# print(number_to_pwr(10, 0), 1)
