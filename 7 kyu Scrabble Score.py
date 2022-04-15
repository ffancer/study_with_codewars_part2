def scrabble_score(st):
    # dict_scores in codewars, dict down for tests in IDE
    dict_scores = {'E': 1, 'A': 1, 'I': 1, 'O': 1, 'N': 1, 'R': 1, 'T': 1, 'L': 1, 'S': 1, 'U': 1, 'D': 2, 'G': 2,
                   'B': 3, 'C': 3,
                   'M': 3, 'P': 3, 'F': 4, 'H': 4, 'V': 4, 'W': 4, 'Y': 4, 'K': 5, 'J': 8, 'X': 8, 'Q': 10, 'Z': 10}

    return sum(dict_scores[i] for i in st.upper() if i in dict_scores.keys())


print(scrabble_score(""), 0, "returns 0 for ''")
print(scrabble_score('a'), 1, 'returns 1 for a')
print(scrabble_score("street"), 6, 'returns 6 for street')
print(scrabble_score("STREET"), 6, 'returns 6 for STREET')
print(scrabble_score(' a'), 1, 'returns score of " a" (with space)')
print(scrabble_score("st re et"), 6, 'returns 6 for street with whitespaces')
