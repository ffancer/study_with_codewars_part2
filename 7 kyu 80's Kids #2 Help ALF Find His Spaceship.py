def find_spaceship(astromap):
    pass


print(type(find_spaceship('X')), list, "Expected the return value to be a list")
print(find_spaceship("X"), [0, 0], "Should work when there is only one place to be")
print(find_spaceship("X\n."), [0, 1], "0,0 is in the BOTTOM left")
print(find_spaceship(".X\n.."), [1, 1])
print(find_spaceship("..\n.X"), [1, 0])
print(find_spaceship("..\nX."), [0, 0])
print(find_spaceship(".......\nX......."), [0, 0])
print(find_spaceship("..........\n..........\n.......X..\n..........\n.........."), [7, 2])
print(find_spaceship("..........\n..........\n..........\n........X.\n.........."), [8, 1])
print(type(find_spaceship('')), str, "Expected the return value to be a String")
print(find_spaceship("........................"), "Spaceship lost forever.", "When there is no ship")
print(find_spaceship("\n\n\n\n"), "Spaceship lost forever.", "When there are no stars.")
