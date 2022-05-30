# 7 kyu
# You Got Change?


def give_change(amount):
    ans = [0, 0, 0, 0, 0, 0]

    while amount > 0:
        ans[5] = amount // 100
        amount -= ans[5] * 100
        ans[4] = amount // 50
        amount -= ans[4] * 50
        ans[3] = amount // 20
        amount -= ans[3] * 20
        ans[2] = amount // 10
        amount -= ans[2] * 10
        ans[1] = amount // 5
        amount -= ans[1] * 5
        ans[0] = amount // 1
        amount -= ans[0] * 1

    return tuple(ans)


print(give_change(365), (0, 1, 1, 0, 1, 3))
print(give_change(217), (2, 1, 1, 0, 0, 2))
