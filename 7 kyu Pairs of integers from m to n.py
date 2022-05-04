def generate_pairs(m, n):
    for i in range(m, n+1):
        for j in range(m, n+1):
            print(i, j)


print(generate_pairs(2, 4), [(2, 2), (2, 3), (2, 4), (3, 3), (3, 4), (4, 4)])
# print(generate_pairs(0, 1), [(0, 0), (0, 1), (1, 1)])
# print(generate_pairs(0, 0), [(0, 0)])
