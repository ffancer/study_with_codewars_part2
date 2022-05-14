def make_acronym(phrase):
    if type(phrase) != str:
        return 'Not a string'

    s = ''

    for i in phrase.split(' '):
        for j in i:
            if j.isdigit():
                return 'Not letters'
        if len(i):
            s += i[0].upper()

    return s


print(make_acronym('My aunt sally'), 'MAS', 'Output not as expected')
print(make_acronym('Please excuse my dear aunt Sally'), 'PEMDAS', 'Output not as expected')
print(make_acronym('How much wood would a woodchuck chuck if a woodchuck could chuck wood'), 'HMWWAWCIAWCCW',
      'Output not as expected')
