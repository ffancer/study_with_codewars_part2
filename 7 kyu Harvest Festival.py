def plant(seed, water, fert, temp):
    return ('-' * water + seed * fert) * water if 20 <= temp <= 30 else ('-' * water) * water + seed


print(plant(",", 3, 7, 25), "---,,,,,,,---,,,,,,,---,,,,,,,")
print(plant("+", 1, 3, 15), "-+")
print(plant(";", 9, 10, 30),
      "---------;;;;;;;;;;---------;;;;;;;;;;---------;;;;;;;;;;---------;;;;;;;;;;---------;;;;;;;;;;---------;;;;;;;;;;---------;;;;;;;;;;---------;;;;;;;;;;---------;;;;;;;;;;")
