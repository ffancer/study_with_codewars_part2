def make_acronym(phrase):
    try:
        s = ''

        if not phrase:
            return ''

        for i in phrase.split():
            s += i[0].upper()

        for i in s:
            if i.isalpha():
                return s
            return 'Not letters'
    except AttributeError:
        return 'Not letters'


print(make_acronym('My aunt sally'), 'MAS', 'Output not as expected')
print(make_acronym('Please excuse my dear aunt Sally'), 'PEMDAS', 'Output not as expected')
print(make_acronym('How much wood would a woodchuck chuck if a woodchuck could chuck wood'), 'HMWWAWCIAWCCW',
      'Output not as expected')
