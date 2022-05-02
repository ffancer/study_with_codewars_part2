def hamming_weight(x):
    return bin(x)[2:].count('1')


print(hamming_weight(10), 2)
print(hamming_weight(21), 3)