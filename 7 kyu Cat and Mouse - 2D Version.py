def cat_mouse(map_, moves):
    return map_.split()


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
