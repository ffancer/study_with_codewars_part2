def decode(code, key):
    lst = []

    for i in code:
        lst.append(chr(i+97))

    return lst
    # return chr(97)


print(decode([20, 12, 18, 30, 21], 1939), "scout")
print(decode([14, 10, 22, 29, 6, 27, 19, 18, 6, 12, 8], 1939), "masterpiece")
