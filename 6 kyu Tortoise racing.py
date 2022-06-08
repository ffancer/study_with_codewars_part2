def race(v1, v2, g):
    if v1 >= v2:
        return None
    else:
        time = g * 3600 / (v2 - v1)
        h = int(time / 3600)
        m = int((time % 3600) / 60)
        s = int(time % 3600 % 60)
        time = [h, m, s]

    return time


print(race(720, 850, 70), [0, 32, 18])
print(race(80, 91, 37), [3, 21, 49])
print(race(820, 81, 550), None)
