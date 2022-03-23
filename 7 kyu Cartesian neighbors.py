def cartesian_neighbor(x, y):
    return [(x-1, y-1), (x-1, y), (x-1, y+1), (), (), (), (), ()]


print(sorted(cartesian_neighbor(2, 2)), [(1, 1), (1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2), (3, 3)])
