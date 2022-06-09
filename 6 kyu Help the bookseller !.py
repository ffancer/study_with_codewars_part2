def stock_list(listOfArt, listOfCat):
    for i in listOfArt:
        if listOfCat in i:
            return i


b = ["ABAR 200", "CDXE 500", "BKWR 250", "BTSQ 890", "DRTY 600"]
c = ["A", "B"]
print(stock_list(b, c), "(A : 200) - (B : 1140)")
