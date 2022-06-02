def calculate_total(t1, t2):
    t1s = sum(t1)
    t2s = sum(t2)
    return t1s > t2s


print(calculate_total([1, 2, 2], [1, 0, 0]), True, 'Calculate the Winner!')
print(calculate_total([6, 45, 1], [1, 55, 0]), False, 'Calculate the Winner!')
print(calculate_total([57, 2, 1], []), True, 'Calculate the Winner!')
print(calculate_total([], [3, 4, 3]), False, 'Calculate the Winner!')
print(calculate_total([], []), False, 'Calculate the Winner!')
