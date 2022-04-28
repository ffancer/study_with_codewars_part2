def sillycase(silly):
    half = (len(silly) + 1) // 2
    return silly[:half].lower() + silly[half:].upper()


print(sillycase('foobar'), "fooBAR")
print(sillycase('codewars'), "codeWARS")
print(sillycase('brian'), 'briAN')
