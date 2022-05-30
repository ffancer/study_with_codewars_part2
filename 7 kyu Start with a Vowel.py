def vowel_start(st):
    vowels = 'ieauo'
    st = ''.join(i for i in st if i.isalpha() or i.isdigit()).lower()
    lst = []

    for i in st:
        if i in vowels:
            lst.append(st)
            st = st[st.find(i)::]
    return lst


print(vowel_start('It is beautiful weather today!'), 'it isb e a ut if ulw e ath ert od ay', )
print(vowel_start('Coding is great'), 'c od ing isgr e at', )
print(vowel_start('my number is 0208-533-2325'), 'myn umb er is02085332325', )
print(vowel_start('oranges, apples, melon, pineapple'), 'or ang es appl esm el onp in e appl e', )
print(vowel_start('under_score'), 'und ersc or e')

