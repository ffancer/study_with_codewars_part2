def solve(a, b):
    pass


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
