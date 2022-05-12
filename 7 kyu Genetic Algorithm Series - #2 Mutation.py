def mutate(chromosome, p):
    return chromosome.replace('1', '0').replace('0', '1')


zero = '0' * 100
one = '1' * 100

print(mutate(zero, 1), one)
print(mutate(one, 1), zero)
print(mutate(zero, 0), zero)
print(mutate(one, 0), one)
# print('0' in mutate(zero, 0.5))
# print('1' in mutate(one, 0.5))
