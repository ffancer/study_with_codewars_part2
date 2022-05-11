from math import ceil


def waterbombs(fire, w):
    if w == 1:
        return fire.count('x')
    return sum(ceil(len(section) / w) for section in fire.split('Y'))


print(waterbombs("xxxxYxYx", 4), 3)
print(waterbombs("xxYxx", 3), 2)
