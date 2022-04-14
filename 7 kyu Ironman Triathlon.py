def i_tri(s):
    if not s:
        return 'Starting Line... Good Luck!'
    elif s >= 140.6:
        return "You're done! Stop running!"

    item_1 = 'Swim' if s <= 2.4 else 'Bike' if s <= 114.4 else 'Run'
    item_2 = 'Nearly there!' if s >= 130.6 else '{0:.2f} to go!'.format(140.6 - s)
    return {item_1: item_2}


print(i_tri(36), {'Bike': '104.60 to go!'})
print(i_tri(103), {'Bike': '37.60 to go!'})
print(i_tri(0), 'Starting Line... Good Luck!')
print(i_tri(2), {'Swim': '138.60 to go!'})
print(i_tri(151), "You're done! Stop running!")
