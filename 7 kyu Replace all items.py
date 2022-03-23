def replace_all(obj, find, replace):
    obj = str(obj)
    obj = obj.replace(str(find), str(replace))
    return [obj]

# print(replace_all([], 1, 2), [])
print(replace_all([1, 2, 2], 1, 2), [2, 2, 2])
print(replace_all([1, 1, 2], 1, 2), [2, 2, 2])
print(replace_all([1, 2, 1, 2, 3], 1, 2), [2, 2, 2, 2, 3])
print(replace_all("Hello World", 'o', '0'), "Hell0 W0rld")
