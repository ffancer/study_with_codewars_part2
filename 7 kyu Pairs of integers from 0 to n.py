from random import randint


def generate_pairs(n):
    n = randint(0, n)
    return n

print(generate_pairs(2), [[0, 0], [0, 1], [0, 2], [1, 1], [1, 2], [2, 2]])
print(generate_pairs(0), [[0, 0]])