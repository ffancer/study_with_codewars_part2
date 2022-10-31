def type_validation(variable, _type):
    return type(variable) == int


print(type_validation(42, "int"), True)
print(type_validation("42", "int"), False)