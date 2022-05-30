# 7 kyu
# You Got Change?


def give_change(amount):
    ans = [0, 0, 0, 0, 0]

    while amount > 0:
        ans[4] = amount // 100
        amount -= ans[4] * 100
        return amount

print(give_change(365), (0, 1, 1, 0, 1, 3))
print(give_change(217), (2, 1, 1, 0, 0, 2))
