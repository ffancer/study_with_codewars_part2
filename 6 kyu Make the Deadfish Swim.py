def parse(data):
    lst = []
    total = 0

    for i in data:
        if i in 'idso':
            if i == 'i':
                total += 1
            if i == 'd':
                total -= 1
            if i == 's':
                total **= 2
            if i == 'o':
                lst.append(total)

    return lst


print(parse("ooo"), [0, 0, 0])
print(parse("ioioio"), [1, 2, 3])
print(parse("idoiido"), [0, 1])
print(parse("isoisoiso"), [1, 4, 25])
print(parse("codewars"), [0])
