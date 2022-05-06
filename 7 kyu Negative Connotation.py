def connotation(strng):
    positive, negative = 0, 0

    for i in strng.split():
        if 109 >= ord(i[0].lower()) >= 97:
            positive += 1
        if 122 >= ord(i[0].lower()) >= 110:
            negative += 1

    return positive >= negative


print(connotation("A big brown fox caught a bad bunny"), True)
print(connotation("Xylophones can obtain Xenon."), False)
print(connotation("CHOCOLATE MAKES A GREAT SNACK"), True)
print(connotation("All FOoD tAsTEs NIcE for someONe"), True)
print(connotation("Is  this the  best  Kata?"), True)
