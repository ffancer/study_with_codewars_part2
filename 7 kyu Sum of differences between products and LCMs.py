def sum_differences_between_products_and_LCMs(pairs):
    ans = 0

    for i, [a, b] in enumerate(pairs):
        product = a * b
        lcm = product
        for j in range(product, max(a - 1, b - a, 1), -max(a, b, 1)):
            if j % a == j % b == 0:
                lcm = j
        ans += product - lcm

    return ans


print(sum_differences_between_products_and_LCMs([[15, 18], [4, 5], [12, 60]]), 840)
print(sum_differences_between_products_and_LCMs([[1, 1], [0, 0], [13, 91]]), 1092)
print(sum_differences_between_products_and_LCMs([[15, 7], [4, 5], [19, 60]]), 0)
print(sum_differences_between_products_and_LCMs([[20, 50], [10, 10], [50, 20]]), 1890)
print(sum_differences_between_products_and_LCMs([]), 0)
