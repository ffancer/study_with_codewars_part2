# def order_weight(strng):
#     pass
#
#
# print(order_weight("103 123 4444 99 2000"), "2000 103 123 4444 99")
# print(order_weight("2000 10003 1234000 44444444 9999 11 11 22 123"),
#       "11 11 2000 10003 22 123 1234000 44444444 9999")
# print(order_weight(""), "")


def sum_dig(n):
    return sum(int(i) for i in str(n))

print(sum_dig(103))
print(sum_dig(44444444))
print(sum_dig(9999))