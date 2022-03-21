def solve(eq):
    return eq[::-1]


print(solve("100*b/y"), "y/b*100")
print(solve("a+b-c/d*30"), "30*d/c-b+a")
print(solve("a*b/c+50"), "50+c/b*a")
