def sentencify(words):
    for i in words:
        if words[0] == "i'm":
            words[0] = "I'm"
        if words[0].islower():
            words[0] = words[0].title()
    return ' '.join(words) + '.'


print(sentencify(["i", "am", "an", "AI"]), "I am an AI.")
print(sentencify(["yes"]), "Yes.")
print(sentencify(["FIELDS", "of", "CORN", "are", "to", "be", "sown"]), "FIELDS of CORN are to be sown.")
print(sentencify(["i'm", "afraid", "I", "can't", "let", "you", "do", "that"]), "I'm afraid I can't let you do that.")
