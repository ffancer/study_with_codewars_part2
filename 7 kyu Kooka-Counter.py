def kooka_counter(laughing):
    return laughing.count('Hah'), laughing.count('haH')


print(kooka_counter(""), 0)
print(kooka_counter("hahahahaha"), 1)
print(kooka_counter("hahahahahaHaHaHa"), 2)
print(kooka_counter("HaHaHahahaHaHa"), 3)
print(kooka_counter("hahahahahahahaHaHa"), 2)
