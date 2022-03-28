def hello_world():
    s = 'Hello, World!'
    lst = []
    for i in s:
        lst.append(ord(i))
    return lst

print(hello_world(), 'Hello, World!')
