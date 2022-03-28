def hello_world():
    lst = [72, 101, 108, 108, 111, 44, 32, 87, 111, 114, 108, 100, 33]
    return ''.join(chr(i) for i in lst)


print(hello_world(), 'Hello, World!')
