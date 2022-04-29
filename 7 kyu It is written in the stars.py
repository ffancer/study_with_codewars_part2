def star_sign(date):
    limits = ['', 20, 19, 20, 20, 21, 21, 22, 23, 23, 23, 22, 21]
    signs = ['Aquarius', 'Pisces', 'Aries', 'Taurus', 'Gemini', 'Cancer', 'Leo', 'Virgo', 'Libra', 'Scorpio',
             'Sagittarius', 'Capricorn']

    if date.day > limits[date.month]:
        return signs[date.month - 1]
    else:
        return signs[date.month - 2]

# print(star_sign(date(1970, 6, 5)), 'Gemini')
# print(star_sign(date(2000, 2, 15)), 'Aquarius')
# print(star_sign(date(1987, 8, 23)), 'Leo')
