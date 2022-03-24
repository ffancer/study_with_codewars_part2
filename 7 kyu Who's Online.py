# 7 kyu
# Who's Online?


def who_is_online(friends):
    return


friends = [{"username": "David", "status": "online", "last_activity": 10},
           {"username": "Lucy", "status": "offline", "last_activity": 22},
           {"username": "Bob", "status": "online", "last_activity": 104}]
print(who_is_online(friends), {"online": ["David"], "offline": ["Lucy"], "away": ["Bob"]})

friends = [{"username": "Lucy", "status": "offline", "last_activity": 22},
           {"username": "Bob", "status": "online", "last_activity": 104}]
print(who_is_online(friends), {"offline": ["Lucy"], "away": ["Bob"]})
