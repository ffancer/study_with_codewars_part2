import sys


def total_bytes(object):
    return sys.getsizeof(object)


print(total_bytes("hello"), 54, "hello")
print(total_bytes(123), 28, 123)
print(total_bytes('[":)", 1]'), 58, '[":)", 1]')
print(total_bytes({'john': 19}), 232, '{"john": 19}')
print(total_bytes("¡◢龘"), 80)
print(total_bytes(999_999), 28)
print(total_bytes((1, 2)), 56)
print(total_bytes("㋛" * 12345), 24764)
