def decode(code, key):
    return ''.join(chr(96 + n - int(str(key)[i % len(str(key))])) for i, n in enumerate(code))


print(decode([20, 12, 18, 30, 21], 1939), "scout")
print(decode([14, 10, 22, 29, 6, 27, 19, 18, 6, 12, 8], 1939), "masterpiece")
