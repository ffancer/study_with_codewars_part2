def presses(phrase):
    phrase = phrase.lower()
    cnt = 0

    for i in phrase:
        if i in '1adgjmptw* #':
            cnt += 1
        elif i in 'behknqux0':
            cnt += 2
        elif i in 'cfilorvy':
            cnt += 3
        elif i in '23456s8z':
            cnt += 4
        elif i in '79':
            cnt += 5

    return cnt


print(presses("LOL"), 9)
print(presses("HOW R U"), 13)
