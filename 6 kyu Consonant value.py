def solve(s):
    ans = 0
    s = s.translate(str.maketrans('aeiou', '00000'))
    s = s.split('0')

    for i in s:
        total = 0
        for j in i:
            total += ord(j) - 96
        if total > ans:
            ans = total

    return ans


print(solve("zodiac"), 26)
print(solve("chruschtschov"), 80)
print(solve("khrushchev"), 38)
print(solve("strength"), 57)
print(solve("catchphrase"), 73)
print(solve("twelfthstreet"), 103)
print(solve("mischtschenkoana"), 80)
