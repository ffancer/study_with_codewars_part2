# 7 kyu
# You Got Change?


def give_change(amount):
    return (amount % 5, (amount % 10) // 5, ((amount % 50) % 20) // 10, (amount % 50) // 20, (amount % 100) // 50,
            amount // 100)


print(give_change(365), (0, 1, 1, 0, 1, 3))
print(give_change(217), (2, 1, 1, 0, 0, 2))
