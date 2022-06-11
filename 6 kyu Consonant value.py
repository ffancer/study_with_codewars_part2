def solve(s):
    vowels = 'aeiou'
    for i in range(len(s)):
        if s[i] + s[i+1] in vowels:




print(solve("zodiac"), 26)
print(solve("chruschtschov"), 80)
print(solve("khrushchev"), 38)
print(solve("strength"), 57)
print(solve("catchphrase"), 73)
print(solve("twelfthstreet"), 103)
print(solve("mischtschenkoana"), 80)
