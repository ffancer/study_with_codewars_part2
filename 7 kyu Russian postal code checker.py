def zipvalidate(postcode):
    for i in ['0', '5', '7', '8', '9']:
        if i in postcode[0]:
            return False
    return True


print(zipvalidate('198328'), True)
print(zipvalidate('310003'), True)
print(zipvalidate('424000'), True)

print(zipvalidate('12A483'), False)
print(zipvalidate('1@63'), False)
print(zipvalidate('111'), False)
print(zipvalidate('056879'), False)
print(zipvalidate('1111111'), False)
