def wrap(value):
    return {'value': value}


print(wrap(res["value"]), "my_test")
print(wrap(343)["value"], 343)
print(wrap(obj)["value"], obj)
