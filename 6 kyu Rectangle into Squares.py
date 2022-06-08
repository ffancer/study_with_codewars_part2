min_max = lambda x, y: (min(x, y), max(x, y))


def sqInRect(lng, wdth):
    if lng == wdth:
        return None
    r, (minimum, maximum) = [], min_max(lng, wdth)

    while True:
        if minimum == 1:
            r += [minimum] * maximum; return r
        elif not maximum % minimum:
            r += [minimum] * (maximum // minimum); return r
        else:
            r.append(minimum); (minimum, maximum) = min_max(minimum, maximum - minimum)


print(sqInRect(5, 5), None)
print(sqInRect(5, 3), [3, 2, 1, 1])
print(sqInRect(20, 14), [14, 6, 6, 2, 2, 2])
print(sqInRect(37, 14), [14, 14, 9, 5, 4, 1, 1, 1, 1])
