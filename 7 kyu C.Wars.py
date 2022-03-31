def initials(name):
    name = name.split()
    lst = []

    for i in name[:-1]:
        lst.append(i[0].upper())

    return lst


print(initials('code wars'), 'C.Wars')
print(initials('Barack hussein obama'), 'B.H.Obama')
print(initials('barack hussein Obama'), 'B.H.Obama')
