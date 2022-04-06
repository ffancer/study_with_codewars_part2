def calculate(string):
    lst = []
    lose = 0

    for i in string.split():
        if i == 'loses':
            lose += 1
        if i.isdigit():
            lst.append(int(i))

    return lst[0] - lst[1] if lose == 1 else sum(lst)


print(calculate("Panda has 48 apples and loses 4"), 44)
print(calculate("Jerry has 34 apples and gains 6"), 40)
print(calculate("Tom has 20 apples and gains 15"), 35)
print(calculate("Fred has 110 bananas and loses 50"), 60)
print(calculate("Pippi has 20 tunas and gains 0"), 20)
