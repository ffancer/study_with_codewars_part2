def play_pass(s, n):
    lst = []

    for i in s:
        lst.append(chr(ord(i) + n))

    return ''.join(lst)

print(play_pass("I LOVE YOU!!!", 1), "!!!vPz fWpM J")
print(play_pass("MY GRANMA CAME FROM NY ON THE 23RD OF APRIL 2015", 2),
      "4897 NkTrC Hq fT67 GjV Pq aP OqTh gOcE CoPcTi aO")
