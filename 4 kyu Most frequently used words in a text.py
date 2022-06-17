def top_3_words(text):
    for i in "//\\,/\ ..?!1234567890:-_;":
        if i in text:
            text = text.replace(i, ' ')

    dct = {}
    text = text.split()

    for j in text:
        j = j.lower()
        if j == '':
            continue
        if "'" in j:
            flag = False
            for k in j:
                if k.isalpha():
                    flag = True
            if not flag:
                continue
        if j not in dct:
            dct[j] = 1
        else:
            dct[j] += 1

    return sorted(dct, key=dct.get, reverse=True)[:3]


print(top_3_words("a a a  b  c c  d d d d  e e e e e"), ["e", "d", "a"])
print(top_3_words("e e e e DDD ddd DdD: ddd ddd aa aA Aa, bb cc cC e e e"), ["e", "ddd", "aa"])
print(top_3_words("  //wont won't won't "), ["won't", "wont"])
print(top_3_words("  , e   .. "), ["e"])
print(top_3_words("  ...  "), [])
print(top_3_words("  '  "), [])
print(top_3_words("  '''  "), [])
print(top_3_words("""In a village of La Mancha, the name of which I have no desire to call to
mind, there lived not long since one of those gentlemen that keep a lance
in the lance-rack, an old buckler, a lean hack, and a greyhound for
coursing. An olla of rather more beef than mutton, a salad on most
nights, scraps on Saturdays, lentils on Fridays, and a pigeon or so extra
on Sundays, made away with three-quarters of his income."""), ["a", "of", "on"])
