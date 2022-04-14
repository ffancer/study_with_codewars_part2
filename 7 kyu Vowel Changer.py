def vowel_change(txt, vow):
    # vowels = 'aeiou'
    s = ''

    for i in txt:
        if i in 'aeiou':
            s += vow
        else:
            s += i

    return s


print(vowel_change("hannah hannah bo-bannah banana fanna fo-fannah fee, fy, mo-mannah. hannah!", 'i'),
      'hinnih hinnih bi-binnih binini finni fi-finnih fii, fy, mi-minnih. hinnih!')
print(vowel_change('adira wants to go to the park', 'o'), 'odoro wonts to go to tho pork')
