def generate_pairs(n):
    lst = list(range(n + 1))
    res = []

    for i in range(0, len(lst)):
        for j in range(0, len(lst)):
            if j >= i:
                res.append([i, j])

    return res


print(generate_pairs(2), [[0, 0], [0, 1], [0, 2], [1, 1], [1, 2], [2, 2]])
print(generate_pairs(0), [[0, 0]])
