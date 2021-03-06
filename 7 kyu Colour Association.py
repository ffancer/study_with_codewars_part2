def colour_association(arr):
    return [{i[0]: i[1]} for i in arr]


print(colour_association([["white", "goodness"], ["blue", "tranquility"]]),
      [{'white': "goodness"}, {'blue': "tranquility"}])
print(colour_association([["red", "energy"], ["yellow", "creativity"], ["brown", "friendly"], ["green", "growth"]]),
      [{'red': "energy"}, {'yellow': "creativity"}, {'brown': "friendly"}, {'green': "growth"}])
print(colour_association([["pink", "compassion"], ["purple", "ambition"]]),
      [{'pink': "compassion"}, {'purple': "ambition"}])
print(colour_association([["gray", "intelligence"], ["black", "classy"]]),
      [{'gray': "intelligence"}, {'black': "classy"}])
print(colour_association([["white", "goodness"], ["blue", "goodness"]]), [{'white': 'goodness'}, {'blue': 'goodness'}])
