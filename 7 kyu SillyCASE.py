from math import ceil


def sillycase(silly):
    mid = ceil(len(silly) / 2)
    return silly[:mid].lower() + silly[mid:].upper()


print(sillycase('foobar'), "fooBAR")
print(sillycase('codewars'), "codeWARS")
print(sillycase('brian'), 'briAN')
