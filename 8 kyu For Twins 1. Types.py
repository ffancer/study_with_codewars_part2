def type_validation(variable, _type):
    types = {'int': int,
             'float': float}
    if _type in types:
        return types[_type]


print(type_validation(42, "int"), True)
print(type_validation("42", "int"), False)