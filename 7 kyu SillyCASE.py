from math import ceil

def sillycase(silly):
    mid = ceil(len(silly) / 2)
    # if len(silly) % 2 != 0:
    #     return silly[:(len(silly)) // 2].lower() + silly[(len(silly) - 1)// 2:].upper()
    # return silly[:len(silly) // 2].lower() + silly[len(silly) // 2:].upper()
    return silly[:mid], silly[mid:]


print(sillycase('foobar'), "fooBAR")
print(sillycase('codewars'), "codeWARS")
print(sillycase('brian'), 'briAN')
