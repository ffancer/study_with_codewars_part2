def connotation(strng):
    positive, negative = 0, 0
    for i in strng.split():
        # print(ord(i[0].lower())) # 97    26 / 2 = 13
        if ord(i[0]) <= 97 + 13:
            positive += 1
        else:
            negative += 1

    return positive , negative


print(connotation("A big brown fox caught a bad bunny"), True)
print(connotation("Xylophones can obtain Xenon."), False)
print(connotation("CHOCOLATE MAKES A GREAT SNACK"), True)
print(connotation("All FOoD tAsTEs NIcE for someONe"), True)
print(connotation("Is  this the  best  Kata?"), True)
