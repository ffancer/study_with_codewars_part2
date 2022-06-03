def char_concat(word):
    cnt = 1
    s = ''

    while word:
        s += word[0]
        s += word[-1]
        s += str(cnt)
        cnt += 1
        word = word[1:-1]

    return s


print(char_concat("abc def"), 'af1be2cd3', "Should work for example test")
print(char_concat("CodeWars"), 'Cs1or2da3eW4', "Should work for 'CodeWars'")
