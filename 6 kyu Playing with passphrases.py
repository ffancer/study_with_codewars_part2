def play_pass(s, n):
    res = ''
    
    for i in map(ord, s):
        if i in range(65, 91):
            res += chr((((i - 65) + n) % 26) + 65)
        elif i in range(97, 123):
            res += chr((((i - 97) + n) % 26) + 97)
        elif i in range(48, 58):
            res += str(abs(9 - int(chr(i))))
        else:
            res += str(chr(i))
    res = ''.join([res[i].upper() if i % 2 == 0 else res[i].lower() for i in range(len(res))])

    return res[::-1]


print(play_pass("I LOVE YOU!!!", 1), "!!!vPz fWpM J")
print(play_pass("MY GRANMA CAME FROM NY ON THE 23RD OF APRIL 2015", 2),
      "4897 NkTrC Hq fT67 GjV Pq aP OqTh gOcE CoPcTi aO")
