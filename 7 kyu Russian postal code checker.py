def zipvalidate(postcode):
    return len(postcode) == 6 and postcode.isdigit() and postcode[0] not in '05789'


print(zipvalidate('198328'), True)
print(zipvalidate('310003'), True)
print(zipvalidate('424000'), True)

print(zipvalidate('12A483'), False)
print(zipvalidate('1@63'), False)
print(zipvalidate('111'), False)
print(zipvalidate('056879'), False)
print(zipvalidate('1111111'), False)
