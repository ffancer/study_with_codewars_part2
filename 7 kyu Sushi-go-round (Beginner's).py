def total_bill(s):
    return s.count('r')


print(total_bill('rr'), 4)
print(total_bill('rr rrr'), 8)
print(total_bill('rr rrr rrr rr'), 16)
print(total_bill('rrrrrrrrrrrrrrrrrr   rr r'), 34)
print(total_bill(''), 0)
