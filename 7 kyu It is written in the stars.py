def star_sign(date):
    month, day = str(date.month), str(date.day)
    return month, day


print(star_sign(date(1970, 6, 5)), 'Gemini')
print(star_sign(date(2000, 2, 15)), 'Aquarius')
print(star_sign(date(1987, 8, 23)), 'Leo')
