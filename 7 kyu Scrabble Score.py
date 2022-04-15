def scrabble_score(st):
    pass


print(scrabble_score(""), 0, "returns 0 for ''")
print(scrabble_score('a'), 1, 'returns 1 for a')
print(scrabble_score("street"), 6, 'returns 6 for street')
print(scrabble_score("STREET"), 6, 'returns 6 for STREET')
print(scrabble_score(' a'), 1, 'returns score of " a" (with space)')
print(scrabble_score("st re et"), 6, 'returns 6 for street with whitespaces')
