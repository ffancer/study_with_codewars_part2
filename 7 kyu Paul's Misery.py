def paul(x):
    dct = {
        'Petes kata': 5,
        'kata': 10,
        'life': 0,
        'eating': 1
    }
    total = 0

    for i in x:
        if i in dct.keys():
            total += dct.get(i)

    return total

print(paul(['life', 'eating', 'life']), 'Super happy!')
print(paul(['life', 'Petes kata', 'Petes kata', 'Petes kata', 'eating']), 'Super happy!')
print(paul(['Petes kata', 'Petes kata', 'eating', 'Petes kata', 'Petes kata', 'eating']), 'Happy!')
