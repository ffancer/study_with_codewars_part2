def comfortable_word(w):
    l, r, w = 'qwertasdfgzxcvb', 'yuiophjklnm', w.lower()
    x = 0 if w[0] in l else 1
    for i in range(len(w)):
        if i % 2 == 0 and w[i] not in (l if x == 0 else r):
            return False
        if i % 2 == 1 and w[i] not in (r if x == 0 else l):
            return False
    return True


print(comfortable_word('yams'), True)
print(comfortable_word('test'), False)
