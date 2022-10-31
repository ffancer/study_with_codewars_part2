def type_validation(variable, _type):
    return type(variable).__name__ == _type


print(type_validation(42, "int"), True)
print(type_validation("42", "int"), False)
print(type_validation(None, "int"), False)
print(type_validation(None, "None"), False)
print(type_validation("42", "int"), False)