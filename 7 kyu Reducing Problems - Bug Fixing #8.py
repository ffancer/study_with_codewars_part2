def calculate_total(t1, t2):
    return sum(t1) > sum(t2)


print(calculate_total([1, 2, 2], [1, 0, 0]), True, 'Calculate the Winner!')
print(calculate_total([6, 45, 1], [1, 55, 0]), False, 'Calculate the Winner!')
print(calculate_total([57, 2, 1], []), True, 'Calculate the Winner!')
print(calculate_total([], [3, 4, 3]), False, 'Calculate the Winner!')
print(calculate_total([], []), False, 'Calculate the Winner!')
