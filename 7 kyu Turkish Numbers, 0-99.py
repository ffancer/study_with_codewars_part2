def get_turkish_number(num):
    dct = {
        0: 'sıfır',
        1: 'bir',
        2: 'iki',
        3: 'üç',
        4: 'dört',
        5: 'beş',
        6: 'altı',
        7: 'yedi',
        8: 'sekiz',
        9: 'dokuz',
        10: 'on',
        20: 'yirmi',
        30: 'otuz',
        40: 'kırk',
        50: 'elli',
        60: 'altmış',
        70: 'yetmiş',
        80: 'seksen',
        90: 'doksan'
    }
    ans = ''


    if num < 10:
        ans = dct.get(num)
    elif num % 10 != 0:
        # ans = f'{int(dct.get(num)) - int(dct.get(num % 10))}{int(dct.get(num % 10))}'
        ans = f'{dct[num - num % 10]} {dct[num % 10]}'
    return ans

print(get_turkish_number(1), "bir")
print(get_turkish_number(13), "on üç")
print(get_turkish_number(27), "yirmi yedi")
print(get_turkish_number(38), "otuz sekiz")
print(get_turkish_number(77), "yetmiş yedi")
print(get_turkish_number(94), "doksan dört")
