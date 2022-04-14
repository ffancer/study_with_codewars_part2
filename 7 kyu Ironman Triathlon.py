def i_tri(s):
    if s <= 2.4:
        return {'Swim': f'{str(140.6 - s).ljust(6, "0")} to go!'}
    if 112 >= s > 2.4:
        return {'Bike': f'{str(round(140.6 - s, 2)).ljust(6, "0")}'}
    if s > 112:


print(i_tri(36), {'Bike': '104.60 to go!'})
print(i_tri(103), {'Bike': '37.60 to go!'})
print(i_tri(0), 'Starting Line... Good Luck!')
print(i_tri(2), {'Swim': '138.60 to go!'})
print(i_tri(151), "You're done! Stop running!")
