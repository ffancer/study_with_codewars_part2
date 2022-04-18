def score_test(tests, right, omit, wrong):
    total = 0

    for i in tests:
        if i == 0:
            total += right
        elif i == 2:
            total -= wrong

    return total


print(score_test([0, 0, 0, 0, 2, 1, 0], 2, 0, 1), 9)
print(score_test([0, 1, 0, 0, 2, 1, 0, 2, 2, 1], 3, -1, 2), 3)
