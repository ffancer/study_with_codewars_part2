def make_acronym(phrase):
    if not phrase:
        return ''
    for i in phrase.split():
        print(i)


print(make_acronym('My aunt sally'), 'MAS', 'Output not as expected')
print(make_acronym('Please excuse my dear aunt Sally'), 'PEMDAS', 'Output not as expected')
print(make_acronym('How much wood would a woodchuck chuck if a woodchuck could chuck wood'), 'HMWWAWCIAWCCW',
      'Output not as expected')
