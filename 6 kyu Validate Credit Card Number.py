validate = lambda n: not sum(
    [0 if x == "0" else (int(x) * 2 - 1) % 9 + 1 if i % 2 else int(x) for i, x in enumerate(reversed(str(n)))]) % 10

print(validate(123), False)
print(validate(1), False)
print(validate(2121), True)
print(validate(1230), True)
