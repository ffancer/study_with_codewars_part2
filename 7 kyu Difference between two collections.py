# return a sorted set with the difference
def diff(a, b):
    lst = []
    for i in list(set(a)):
        if i in list(set(b)):
            pass
        else:
            lst.append(i)
    return lst

print(diff(['a', 'b'], ['a', 'b']), [])
a = ['a', 'b']
b = []
print(diff(a, b), a)
a = []
b = ['a', 'b']
print(diff(a, b), b)
print(diff([], []), [])
a = ['a', 'b', 'z']
b = ['a', 'b']
print(diff(a, b), ['z'])
a = ['a', 'b', 'z', 'd', 'e', 'd']
b = ['a', 'b', 'j', 'j']
print(diff(a, b), ['d', 'e', 'j', 'z'])
