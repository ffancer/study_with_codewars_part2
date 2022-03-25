def complete_series(seq):
    second_seq = list(set(seq))

    if len(seq) != len(second_seq):
        return [0]
    return [i for i in range(max(seq) + 1)]


print(complete_series([0, 1]), [0, 1])
print(complete_series([1, 4, 6]), [0, 1, 2, 3, 4, 5, 6])
print(complete_series([3, 4, 5]), [0, 1, 2, 3, 4, 5])
print(complete_series([2, 1]), [0, 1, 2])
print(complete_series([1, 4, 4, 6]), [0])
