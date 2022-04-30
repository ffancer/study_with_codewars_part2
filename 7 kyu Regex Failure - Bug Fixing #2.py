from re import sub


def filter_words(phrase):
    phrase = sub("(bad|mean|ugly|horrible|hideous)", "awesome", phrase.lower())
    return phrase[0].upper() + phrase[1:].replace('soo', 'Soo')


print(filter_words("You're Bad! timmy!"), "You're awesome! timmy!")
print(filter_words("You're MEAN! timmy!"), "You're awesome! timmy!")
