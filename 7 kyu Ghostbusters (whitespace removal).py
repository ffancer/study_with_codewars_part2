def ghostbusters(building):
    if building.count(' ') > 0:
        s = ''

        for i in building:
            if i != ' ':
                s += i
        return s

    return "You just wanted my autograph didn't you?"


print(ghostbusters("Factor y"), "Factory", 'Nope, there may still be a ghost in the building. Try again.')
print(ghostbusters("O  f fi ce"), "Office", 'Nope, there may still be a ghost in the building. Try again.')
print(ghostbusters("BusStation"), "You just wanted my autograph didn't you?",
      'Nope, as there were no ghosts in the BusStation you need to return a witty retort.')
