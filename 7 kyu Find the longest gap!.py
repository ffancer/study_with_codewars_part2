def gap(num):
    num = bin(num)[2:].rstrip('0')
    return len(max(num.split('1'), key=len))


print(gap(9), 2)
print(gap(529), 4)
print(gap(20), 1)
print(gap(15), 0)
