def count_salutes(hallway):
    return hallway.replace('-', '')



print(count_salutes('>--->---<--<'), 8)
print(count_salutes('<----<---<-->'), 0)
print(count_salutes('>-<->-<'), 6)
