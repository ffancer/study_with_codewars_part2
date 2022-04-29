def star_sign(date):
    month, day = str(date.month), str(date.day)

    if len(day) < 2:
        day = '0' + day
    birth = int(month + day)

    if 121 <= birth <= 219:
        return 'Aquarius'
    elif 220 <= birth <= 320:
        return 'Pisces'
    elif 321 <= birth <= 420:
        return 'Aries'
    elif 421 <= birth <= 521:
        return 'Taurus'
    elif 522 <= birth <= 621:
        return 'Gemini'
    elif 622 <= birth <= 722:
        return 'Cancer'
    elif 723 <= birth <= 823:
        return 'Leo'
    elif 824 <= birth <= 923:
        return 'Virgo'
    elif 924 <= birth <= 1023:
        return 'Libra'
    elif 1024 <= birth <= 1122:
        return 'Scorpio'
    elif 1123 <= birth <= 1221:
        return 'Sagittarius'
    else:
        return 'Capricorn'

# print(star_sign(date(1970, 6, 5)), 'Gemini')
# print(star_sign(date(2000, 2, 15)), 'Aquarius')
# print(star_sign(date(1987, 8, 23)), 'Leo')
