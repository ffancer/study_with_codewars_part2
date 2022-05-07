def solve(a, b):
    if a == b:
        return True
    if len(a) > len(b) + 1:
        return False
    try:
        i = a.index('*')
        j = a[::-1].index('*')
        k = a[-1:-j - 1: -1]
        return a[:i] == b[:i] and k == b[::-1][:len(k)]
    except ValueError:
        return False


print(solve("code*s", "codewars"), True)
print(solve("codewar*s", "codewars"), True)
print(solve("code*warrior", "codewars"), False)
print(solve("c", "c"), True)
print(solve("*s", "codewars"), True)
print(solve("*s", "s"), True)
print(solve("s*", "s"), True)
print(solve("aa", "aaa"), False)
print(solve("aa*", "aaa"), True)
print(solve("aaa", "aa"), False)
print(solve("aaa*", "aa"), False)
print(solve("*", "codewars"), True)
