# Make sure you follow the order of reaction
# output should be H2O,CO2,CH4
def burner(c, h, o):
    water = 0
    carbon_dioxide = 0
    methane = 0

    while h > 1 and o > 0:
        h -= 2
        o -= 1
        water += 1

    while c > 0 and o > 1:
        c -= 1
        o -= 2
        carbon_dioxide += 1

    while c > 0 and h > 3:
        c -= 1
        h -= 4
        methane += 1


    return water, carbon_dioxide, methane


print(burner(45, 11, 100), (5, 45, 0))
print(burner(354, 1023230, 0), (0, 0, 354))
print(burner(939, 3, 694), (1, 346, 0))
