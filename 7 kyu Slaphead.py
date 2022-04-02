def bald(s):
    cnt_stray = s.count('/')
    lst = [s.replace('/', '-')]
    return lst

print(bald("/---------"), "Unicorn!", )
print(bald("/-----/-"), "Homer!", )
print(bald("--/--/---/-/---"), "Careless!", )
