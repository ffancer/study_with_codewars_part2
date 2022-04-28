def sillycase(silly):
    return silly[:len(silly)//2]


print(sillycase('foobar'), "fooBAR")
print(sillycase('codewars'), "codeWARS")
print(sillycase('brian'), 'briAN')
