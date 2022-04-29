def cat_mouse(map_, moves):
    road = map_.split('\n')
    cat, mouse = None, None

    for i in range(len(road)):
        for j in range(len(road[0])):
            if road[i][j] == 'C':
                cat = [i, j]
            elif road[i][j] == 'm':
                mouse = [i, j]

    if cat and mouse:
        return 'Caught!' if abs(cat[0] - mouse[0]) + abs(cat[1] - mouse[1]) <= moves else 'Escaped!'
    return 'boring without two animals'


map_ = '''\
..C......
.........
....m....'''
print(cat_mouse(map_, 5), 'Caught!')

map_ = '''\
.C.......
.........
......m..'''
print(cat_mouse(map_, 5), 'Escaped!')

map_ = '''\
..C......
.........
.........'''
print(cat_mouse(map_, 5), 'boring without two animals')
