def grid_map(inp, op):
    lst = []

    for i in inp:
        lst.append(list(map(op, i)))

    return lst


num_grid = [[1, 2, 3, 4], [5, 6, 7, 8, 9], [0, 2, 4]]
char_grid = [['h', 'E', 'l', 'l', 'O'], ['w', 'O', 'r', 'L', 'd']]

print(grid_map(num_grid, lambda x: x + 1))
