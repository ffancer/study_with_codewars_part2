def capitals_first(text):
    text = text.split()
    lst_upper, lst_lower = [], []

    for i in text:
        if i[0].isupper():
            lst_upper.append(i)

        if i[0].islower():
            lst_lower.append(i)

    return ' '.join(lst_upper + lst_lower)


print(capitals_first("sense Does to That Make you?"), "Does That Make sense to you?")
