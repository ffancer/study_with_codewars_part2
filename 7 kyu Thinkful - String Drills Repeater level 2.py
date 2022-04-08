def repeater(string, n):
    return f'"{string}" repeated {n} times is: "{string * n}"'


print(repeater('yo', 3), '"yo" repeated 3 times is: "yoyoyo"')
print(repeater('WuB', 6), '"WuB" repeated 6 times is: "WuBWuBWuBWuBWuBWuB"')
print(repeater('code, eat, code, sleep... ', 2),
      '"code, eat, code, sleep... " repeated 2 times is: "code, eat, code, sleep... code, eat, code, sleep... "')
