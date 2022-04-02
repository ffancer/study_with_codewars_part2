def reverse(a):
    lst, i = [], 0
    letters = ''.join(a)[::-1]

    for k in a:
        lst.append(letters[i:i + len(k)])
        i += len(k)

    return lst




print(reverse(["I", "like", "big", "butts", "and", "I", "cannot", "lie!"]),
      ["!", "eilt", "onn", "acIdn", "ast", "t", "ubgibe", "kilI"])

print(reverse(
    ["?kn", "ipnr", "utotst", "ra", "tsn", "iksr", "uo", "yer", "ofebta", "eote", "vahu", "oyodpm", "ir", "hsyn",
     "amwoH"]),
      ["How", "many", "shrimp", "do", "you", "have", "to", "eat", "before", "your", "skin", "starts", "to", "turn",
       "pink?"])
