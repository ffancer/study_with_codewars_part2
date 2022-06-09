def stock_list(listOfArt, listOfCat):
    if len(listOfArt) == 0 or len(listOfCat) == 0:
        return ''

    letter_dct = dict()

    for i in listOfArt:
        if i[0:1] in letter_dct:
            letter_dct[i[0:1]] += int(i.split(" ")[1])
        else:
            letter_dct[i[0:1]] = int(i.split(" ")[1])

    s = ''

    for i in listOfCat:
        num = 0
        if i in letter_dct:
            num = letter_dct[i]
        s += f"({i} : {num}) - "

    return s[0:len(s)-3]


b = ["ABAR 200", "CDXE 500", "BKWR 250", "BTSQ 890", "DRTY 600"]
c = ["A", "B"]
print(stock_list(b, c), "(A : 200) - (B : 1140)")
