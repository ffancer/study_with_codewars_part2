def paul(x):
    dct = {
        'Petes kata': 10,
        'kata': 5,
        'life': 0,
        'eating': 1
    }
    total = sum([dct.get(i) for i in x])

    return 'Super happy!' if total < 40 else 'Happy!' if total < 70 else 'Sad!' if total < 100 else 'Miserable!'


print(paul(['life', 'eating', 'life']), 'Super happy!')
print(paul(['life', 'Petes kata', 'Petes kata', 'Petes kata', 'eating']), 'Super happy!')
print(paul(['Petes kata', 'Petes kata', 'eating', 'Petes kata', 'Petes kata', 'eating']), 'Happy!')
