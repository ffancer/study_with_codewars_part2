from random import randint


def generate(length):
    res = ''

    while len(res) < length:
        res += str(round(randint(0, 1)))

    return res


print(generate(16), 16)
print(generate(32), 32)
print(generate(64), 64)
