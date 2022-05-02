def zipvalidate(postcode):
    if len(postcode) == 6:
        if postcode.isdigit():
            if postcode[0] not in '05789':
                return True
    return False


print(zipvalidate('198328'), True)
print(zipvalidate('310003'), True)
print(zipvalidate('424000'), True)

print(zipvalidate('12A483'), False)
print(zipvalidate('1@63'), False)
print(zipvalidate('111'), False)
print(zipvalidate('056879'), False)
print(zipvalidate('1111111'), False)
