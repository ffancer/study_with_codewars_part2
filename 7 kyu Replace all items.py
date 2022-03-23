def replace_all(obj, find, replace):
    if obj is []:
        return []
    if type(obj[0]) == str:
        obj = str(obj)
        obj = obj.replace(str(find), str(replace))
        return obj
    if type(obj[0]) == int:
        lst = []
        for i in obj:
            if i == find:
                lst.append(replace)
            else:
                lst.append(i)
        return lst


print(replace_all([], 1, 2), [])
print(replace_all([1, 2, 2], 1, 2), [2, 2, 2])
print(replace_all([1, 1, 2], 1, 2), [2, 2, 2])
print(replace_all([1, 2, 1, 2, 3], 1, 2), [2, 2, 2, 2, 3])
print(replace_all("Hello World", 'o', '0'), "Hell0 W0rld")
