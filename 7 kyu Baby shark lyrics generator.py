def baby_shark_lyrics():
    shark = ' shark'
    dct = {'Baby': shark, 'Mommy': shark, 'Daddy': shark, 'Grandma': shark, 'Grandpa': shark, 'Let\'s go hunt': ''}
    ans = ''

    for i, j in dct.items():
        ans += '{}{},{}\n'.format(i, j, ' doo' * 6) * 3
        ans += '{}{}!\n'.format(i, j)
    ans += 'Run away,…'

    return ans


babyshark = '''Baby shark, doo doo doo doo doo doo
Baby shark, doo doo doo doo doo doo
Baby shark, doo doo doo doo doo doo
Baby shark!
Mommy shark, doo doo doo doo doo doo
Mommy shark, doo doo doo doo doo doo
Mommy shark, doo doo doo doo doo doo
Mommy shark!
Daddy shark, doo doo doo doo doo doo
Daddy shark, doo doo doo doo doo doo
Daddy shark, doo doo doo doo doo doo
Daddy shark!
Grandma shark, doo doo doo doo doo doo
Grandma shark, doo doo doo doo doo doo
Grandma shark, doo doo doo doo doo doo
Grandma shark!
Grandpa shark, doo doo doo doo doo doo
Grandpa shark, doo doo doo doo doo doo
Grandpa shark, doo doo doo doo doo doo
Grandpa shark!
Let's go hunt, doo doo doo doo doo doo
Let's go hunt, doo doo doo doo doo doo
Let's go hunt, doo doo doo doo doo doo
Let's go hunt!
Run away,…'''

print(baby_shark_lyrics(), babyshark)
