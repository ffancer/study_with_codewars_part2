def score_per_lines_cleared(lines_cleared, level):
    level += 1
    if lines_cleared == 1:
        return 40 * level
    elif lines_cleared == 2:
        return 100 * level
    elif lines_cleared == 3:
        return 300 * level
    elif lines_cleared == 4:
        return 1200 * level
    return 0


def get_score(arr):
    ret = 0
    level = 0
    total_lines = 0
    for lines_cleared in arr:
        ret += score_per_lines_cleared(lines_cleared, level)
        total_lines += lines_cleared
        level = total_lines // 10
    return ret


print(get_score([0, 1, 2, 3, 4]), 1640)
print(get_score([0, 1, 1, 3, 0, 2, 1, 2]), 620)
print(get_score([2, 0, 4, 2, 2, 3, 0, 0, 3, 3]), 3300)
print(get_score([0]), 0)
print(get_score([]), 0)
