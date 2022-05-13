def direction(facing, turn):
    lst = ['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW']
    turn %= 360

    return lst[(lst.index(facing) + (turn//45)) % len(lst)]


print(direction("S", 180), "N")
print(direction("SE", -45), "E")
print(direction("W", 495), "NE")
