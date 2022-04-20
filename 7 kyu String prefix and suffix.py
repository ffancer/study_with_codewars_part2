def solve(st):
    s = len(st)

    for i in range(s // 2, 0, -1):
        prefix = st[:i]
        suffix = st[i:]
        print(suffix)


print(solve("abcd"), 0)
print(solve("abcda"), 1)
print(solve("abcdabc"), 3)
print(solve("abcabc"), 3)
print(solve("abcabca"), 1)
print(solve("aaaaa"), 2)
print(solve("aaaa"), 2)
print(solve("aaa"), 1)
print(solve("aa"), 1)
print(solve("a"), 0)
