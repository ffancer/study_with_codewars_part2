def generate_pairs(n):
    return [[i,j] for i in range(n+1) for j in range(i, n+1)]


print(generate_pairs(2), [[0, 0], [0, 1], [0, 2], [1, 1], [1, 2], [2, 2]])
print(generate_pairs(0), [[0, 0]])
