def filter_long_words(sentence, n):
    return [i for i in sentence.split() if len(i) > n]


print(filter_long_words("The quick brown fox jumps over the lazy dog", 4), ['quick', 'brown', 'jumps'])
