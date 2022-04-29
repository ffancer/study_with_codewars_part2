def append_arrays(seq1, seq2):
    return seq1 + seq2


print(append_arrays([1, 2], [2, 4]), [1, 2, 2, 4])
print(append_arrays([1, 2], [3, 4]), [1, 2, 3, 4])
print(append_arrays(['this'], ['that']), ['this', 'that'])
print(append_arrays(['a', 'B'], ['c', 'D']), ['a', 'B', 'c', 'D'])
print(append_arrays([1, 2], [1]), [1, 2, 1])
