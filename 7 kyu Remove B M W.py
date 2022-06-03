def remove_bmw(string):
    try:
        for i in string:
            if i in 'BMWbmw':
                string = string.replace(i, '')
        return string
    except TypeError:
        return "This program only works for text."


print(remove_bmw("bmwvolvoBMW"), "volvo")
print(remove_bmw("blablahblah"), "lalahlah")
