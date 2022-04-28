def sillycase(silly):
    if len(silly) % 2 != 0:
        return silly[:(len(silly) // 2)].lower() + silly[len(silly) // 2:].upper()
    return silly[:len(silly) // 2].lower() + silly[len(silly) // 2:].upper()


print(sillycase('foobar'), "fooBAR")
print(sillycase('codewars'), "codeWARS")
print(sillycase('brian'), 'briAN')
