# 7 kyu
# How many days are we represented in a foreign country?


def days_represented(trips):
    s = set()

    for i in trips:
        s.update(range(i[0], i[1] + 1))

    return len(s)


print(days_represented([[10, 15], [25, 35]]), 17)
print(days_represented([[2, 8], [220, 229], [10, 16]]), 24)
