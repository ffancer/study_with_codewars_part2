def to_binary(n):
    return '{:b}'.format(n & 4294967295)


print(to_binary(2), "10")
print(to_binary(3), "11")
print(to_binary(4), "100")
print(to_binary(-3), "11111111111111111111111111111101")
print(to_binary(0), "0")
