def connotation(strng):
    for i in strng.split():
        print(i[0].lower())


print(connotation("A big brown fox caught a bad bunny"), True)
print(connotation("Xylophones can obtain Xenon."), False)
print(connotation("CHOCOLATE MAKES A GREAT SNACK"), True)
print(connotation("All FOoD tAsTEs NIcE for someONe"), True)
print(connotation("Is  this the  best  Kata?"), True)
