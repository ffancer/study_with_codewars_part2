grid = ['top left', 'top middle', 'top right',
        'middle left', 'center', 'middle right',
        'bottom left', 'bottom middle', 'bottom right']


def fire(x, y):
    return grid[x + 3 * y]


print(fire(0, 0), "top left")
print(fire(1, 1), "center")
