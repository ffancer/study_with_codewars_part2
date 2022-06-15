def snail(snail_map):
    if snail_map == [[]]:
        return []
    lst = []

    while len(snail_map) > 0:
        lst += snail_map[0]
        del snail_map[0]
        if len(snail_map) <= 0:
            break
        for row in snail_map:
            lst += [row[-1]]
            del row[-1]
        if len(snail_map) <= 0:
            break
        lst += snail_map[-1][::-1]
        del snail_map[-1]
        if len(snail_map) <= 0:
            break
        for row in reversed(snail_map):
            lst += [row[0]]
            del row[0]
    return lst


array = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]
expected = [1, 2, 3, 6, 9, 8, 7, 4, 5]
print(snail(array), expected)

array = [[1, 2, 3],
         [8, 9, 4],
         [7, 6, 5]]
expected = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(snail(array), expected)
