# 7 kyu
# Hamming Distance - Part 1: Binary codes


def hamming_distance(a, b):
    cnt, i = 0, 0

    while i < len(a):
        if a[i] != b[i]:
            cnt += 1
        i += 1

    return cnt


print(hamming_distance('100101', '101001'), 2)
print(hamming_distance('1010', '0101'), 4)
print(hamming_distance('100101011011010010010', '101100010110010110101'), 9)
