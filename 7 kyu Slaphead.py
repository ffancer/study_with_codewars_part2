def bald(s):
    cnt_stray = s.count('/')
    return s.replace('/', '-')

print(bald("/---------"), "Unicorn!", )
print(bald("/-----/-"), "Homer!", )
print(bald("--/--/---/-/---"), "Careless!", )
