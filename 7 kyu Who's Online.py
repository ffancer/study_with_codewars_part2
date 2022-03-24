# 7 kyu
# Who's Online?


def who_is_online(friends):
    if not friends:
        return {}

    dct = {}

    for i in friends:
        if i['status'] == 'online':
            if i['last_activity'] > 10:
                if 'away' not in dct.keys():
                    dct['away'] = []
                dct['away'].append(i['username'])
            else:
                if 'online' not in dct.keys():
                    dct['online'] = []
                dct['online'].append(i['username'])
        elif i['status'] == 'offline':
            if 'offline' not in dct.keys():
                dct['offline'] = []
            dct['offline'].append(i['username'])
    return dct


friends = [{"username": "David", "status": "online", "last_activity": 10},
           {"username": "Lucy", "status": "offline", "last_activity": 22},
           {"username": "Bob", "status": "online", "last_activity": 104}]
print(who_is_online(friends), {"online": ["David"], "offline": ["Lucy"], "away": ["Bob"]})

friends = [{"username": "Lucy", "status": "offline", "last_activity": 22},
           {"username": "Bob", "status": "online", "last_activity": 104}]
print(who_is_online(friends), {"offline": ["Lucy"], "away": ["Bob"]})
