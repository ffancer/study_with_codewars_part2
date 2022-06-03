def reverse_list(lst):
    pass


tests = (
    ([], []),
    ([1, 2, 3, 4], [4, 3, 2, 1]),
    ([2, 4, 5, 6], [6, 5, 4, 2]),
)

for t in tests:
    inp, exp = t
    print(reverse_list(inp), exp)
