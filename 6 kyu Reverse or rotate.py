# 6 kyu
# Reverse or rotate?


def revrot(s, n, res=""):
    if not s or n < 1 or n > len(s):
        return ""

    while len(s) >= n:
        group = s[:n]
        if sum([int(d) ** 3 for d in group]) % 2 == 0:
            res += group[::-1]
        else:
            res += group[1:] + group[0]
        s = s[n:]

    return res


print(revrot("1234", 0), "")
print(revrot("", 0), "")
print(revrot("1234", 5), "")
s = "733049910872815764"
print(revrot(s, 5), "330479108928157")
