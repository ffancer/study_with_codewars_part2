points = [0, 40, 100, 300, 1200]


def get_score(arr):
    cleared = 0
    score = 0

    for i in arr:
        level = cleared // 10
        score += (level+1) * points[i]
        cleared += i

    return score


print(get_score([0, 1, 2, 3, 4]), 1640)
print(get_score([0, 1, 1, 3, 0, 2, 1, 2]), 620)
print(get_score([2, 0, 4, 2, 2, 3, 0, 0, 3, 3]), 3300)
print(get_score([0]), 0)
print(get_score([]), 0)
