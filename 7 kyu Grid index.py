def grid_index(grid, indexes):
    letters = [j for i in grid for j in i]
    return letters

results1 = grid_index([['m', 'y', 'e'], ['x', 'a', 'm'], ['p', 'l', 'e']], [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(results1, 'myexample')
results2 = grid_index([['m', 'y', 'e'], ['x', 'a', 'm'], ['p', 'l', 'e']], [1, 5, 6])
print(results2, 'mam')
results3 = grid_index([['m', 'y', 'e'], ['x', 'a', 'm'], ['p', 'l', 'e']], [1, 3, 7, 8])
print(results3, 'mepl')
results4 = grid_index([['h', 'e', 'l', 'l'], ['o', 'c', 'o', 'd'], ['e', 'w', 'a', 'r'], ['r', 'i', 'o', 'r']],
                      [5, 7, 9, 3, 6, 6, 8, 8, 16, 13])
print(results4, 'ooelccddrr')
