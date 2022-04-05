def gap(num):
    return len(max(bin(num)[2:].split('1'), key=len))
    # return bin(num)[2:]

print(gap(9), 2)
print(gap(529), 4)
print(gap(20), 1)
print(gap(15), 0)
