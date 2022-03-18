def mod256_without_mod(number):
    return number - number // 256 * 256


print(mod256_without_mod(254), 254)
print(mod256_without_mod(256), 0)
print(mod256_without_mod(258), 2)
print(mod256_without_mod(-254), 2)
print(mod256_without_mod(-256), 0)
print(mod256_without_mod(-258), 254)
