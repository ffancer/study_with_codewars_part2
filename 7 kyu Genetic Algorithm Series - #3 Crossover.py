def crossover(chromosome1, chromosome2, index):
    if len(chromosome1) % 2 == 0:

        return [chromosome1[:index]+chromosome2[index:], chromosome1[index:]+chromosome2[:index]]


print(crossover("110", "001", 2), ["111", "000"])
print(crossover("111000", "000110", 3), ["111110", "000000"])
