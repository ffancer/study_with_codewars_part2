from re import sub
def filter_words(phrase):
    return sub("(bad|mean|ugly|horrible|hideous)","awesome",phrase)


print(filter_words("You're Bad! timmy!"),"You're awesome! timmy!")
print(filter_words("You're MEAN! timmy!"),"You're awesome! timmy!")