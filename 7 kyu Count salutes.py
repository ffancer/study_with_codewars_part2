def count_salutes(hallway):
    lst = list(hallway.replace('-', ''))
    cnt = 0

    for i in range(0, len(lst) - 1):
        for j in range(1, len(lst)):
            if lst[i] + lst[j] == '><' and j > i:
                cnt += 2

    return cnt


print(count_salutes('>--->---<--<'), 8)
print(count_salutes('<----<---<-->'), 0)
print(count_salutes('>-<->-<'), 6)
