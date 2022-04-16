# def shared_bits(a, b):
#     lst_a, lst_b = list(bin(a)[2:]), list(bin(b)[2:])
#     # lst_a = [int(i) for i in lst_a]
#     # lst_b = [int(i) for i in lst_b]
#     cnt = 0
#     # for i in range(len(lst_a)):
#     #     for j in range(len(lst_b)):
#     #         if lst_a[i] == lst_b[j] == 1:
#     #             cnt += 1
#
#     # matches = list(i for i in zip(lst_a, lst_b))
#     # return matches


def shared_bits(a, b):
  a, b = bin(a)[2:], bin(b)[2:]
  dct_a, dct_b = {i: a[i] for i in range(len(a))}, {i: b[i] for i in range(len(b))}
  return dct_a, dct_b

print(shared_bits(1, 2), False)
print(shared_bits(16, 8), False)
print(shared_bits(1, 1), False)
print(shared_bits(2, 3), False)
print(shared_bits(7, 10), False)
print(shared_bits(43, 77), True)
print(shared_bits(7, 15), True)
print(shared_bits(23, 7), True)
