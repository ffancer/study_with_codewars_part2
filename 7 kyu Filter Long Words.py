def filter_long_words(sentence, n):
    sentence = sentence.split()
    lst = []

    for i in sentence:
        if len(i) > n:
            lst.append(i)

    return lst


print(filter_long_words("The quick brown fox jumps over the lazy dog", 4), ['quick', 'brown', 'jumps'])
