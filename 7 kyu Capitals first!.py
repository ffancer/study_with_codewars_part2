def capitals_first(text):
    return ' '.join(sorted(text.split(), key=str.upper))


print(capitals_first("sense Does to That Make you?"), "Does That Make sense to you?")
