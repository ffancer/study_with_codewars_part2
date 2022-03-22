def well(arr):
    cnt = 0

    for i, j in enumerate(arr):
        for k in j:
            if str(k).lower() == 'good':
                cnt += 1

    if cnt == 1 or cnt == 2:
        return 'Publish!'
    if cnt > 2:
        return 'I smell a series!'
    return 'Fail!'


print(well([['bad', 'bAd', 'bad'], ['bad', 'bAd', 'bad'], ['bad', 'bAd', 'bad']]), 'Fail!')
print(well([['gOOd', 'bad', 'BAD', 'bad', 'bad'], ['bad', 'bAd', 'bad'], ['GOOD', 'bad', 'bad', 'bAd']]),
      'Publish!')
print(well([['gOOd', 'bAd', 'BAD', 'bad', 'bad', 'GOOD'], ['bad'], ['gOOd', 'BAD']]), 'I smell a series!')
