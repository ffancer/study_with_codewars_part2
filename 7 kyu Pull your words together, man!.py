def sentencify(words):
    res = ' '.join(words) + '.'
    return res[0].upper() + res[1:]


print(sentencify(["i", "am", "an", "AI"]), "I am an AI.")
print(sentencify(["yes"]), "Yes.")
print(sentencify(["FIELDS", "of", "CORN", "are", "to", "be", "sown"]), "FIELDS of CORN are to be sown.")
print(sentencify(["i'm", "afraid", "I", "can't", "let", "you", "do", "that"]), "I'm afraid I can't let you do that.")
