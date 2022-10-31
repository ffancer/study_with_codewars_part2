def type_validation(variable, _type):
    if _type == 'int':
        _type = int
    elif _type == 'float':
        _type = float
    elif _type == bool:
        _type = bool
    elif _type == list:
        _type = list
    elif _type == dict:
        _type = dict
    elif _type is None:
        _type = None
    elif _type is set:
        _type = set
    elif _type is tuple:
        _type = tuple
    return _type == type(variable)

print(type_validation(42, "int"), True)
print(type_validation("42", "int"), False)
print(type_validation(None, "int"), False)
print(type_validation(None, "None"), False)
print(type_validation("42", "int"), False)