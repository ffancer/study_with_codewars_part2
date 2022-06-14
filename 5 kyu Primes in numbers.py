def prime_factors(n):
    dct = {}

    for i in range(2, n + 1):
        while n % i == 0 and n >= 1:
            if i in dct:
                dct[i] += 1
            else:
                dct[i] = 1
            n /= i

    return dct


print(prime_factors(7775460), "(2**2)(3**3)(5)(7)(11**2)(17)")
