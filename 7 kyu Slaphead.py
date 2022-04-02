def bald(s):
    cnt = s.count('/')
    lst = [s.replace('/', '-')]

    if cnt == 0: lst.append("Clean!")
    if cnt == 1: lst.append("Unicorn!")
    if cnt == 2: lst.append("Homer!")
    if 5 >= cnt >= 3: lst.append("Careless!")
    if cnt > 5: lst.append("Hobo!")

    return lst

print(bald("/---------"), "Unicorn!", )
print(bald("/-----/-"), "Homer!", )
print(bald("--/--/---/-/---"), "Careless!", )
