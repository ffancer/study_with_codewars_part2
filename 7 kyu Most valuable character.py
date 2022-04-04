def solve(strng):
    pos = [(len(strng) - strng[::-1].index(i) - strng.index(i), i) for i in set(strng)]
    return max(pos, key=lambda item: (item[0], ord('z') - ord(item[1])))[1]


print(solve('a'), 'a')
print(solve('aa'), 'a')
print(solve('bcd'), 'b')
print(solve('axyzxyz'), 'x')
print(solve('aabccc'), 'c')
