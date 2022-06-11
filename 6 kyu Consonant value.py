def solve(s):
    val = 0

    s = s.translate(str.maketrans('aeiou', '00000'))
    return s


print(solve("zodiac"), 26)
print(solve("chruschtschov"), 80)
print(solve("khrushchev"), 38)
print(solve("strength"), 57)
print(solve("catchphrase"), 73)
print(solve("twelfthstreet"), 103)
print(solve("mischtschenkoana"), 80)
